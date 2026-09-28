#!/usr/bin/env python3
"""Render the Taste Trip dataset overview figure (light + dark variants) for the portfolio README.

Source data: data/Item_data.xlsx in the public `jiheon` branch of
https://github.com/heoneyzi/Taste_Trip_Recommender-System (commit 23d8e10, "initial data from daiv project").
Only aggregate counts are plotted (venues per area group and type; most frequent review-keyword tags).

Usage (from a clone that has fetched the jiheon branch):
    git -C <clone> show origin/jiheon:data/Item_data.xlsx > Item_data.xlsx
    python make_dataset_overview.py Item_data.xlsx .
"""
import sys, os, collections
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.path import Path
from matplotlib.patches import PathPatch

FONT = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
if os.path.exists(FONT):
    font_manager.fontManager.addfont(FONT)
    plt.rcParams['font.family'] = font_manager.FontProperties(fname=FONT).get_name()

THEMES = {
    'light': dict(surface='#fcfcfb', ink='#0b0b0b', ink2='#52514e', muted='#898781', grid='#e1e0d9',
                  base='#c3c2b7', s1='#2a78d6', s2='#eb6834'),
    'dark': dict(surface='#1a1a19', ink='#ffffff', ink2='#c3c2b7', muted='#898781', grid='#2c2c2a',
                 base='#383835', s1='#3987e5', s2='#d95926'),
}
AREA_LABELS = {'선유도역, 당산역': '선유도역·당산역\nSeonyudo / Dangsan stn.', '목1동': '목1동\nMok 1-dong',
               '목동': '목동\nMok-dong', '그외': '그외\nother areas', '목2동': '목2동\nMok 2-dong'}
TAG_EN = {'친절해요': 'friendly staff', '음식이 맛있어요': 'tasty food', '인테리어가 멋져요': 'nice interior',
          '매장이 청결해요': 'clean', '재료가 신선해요': 'fresh ingredients', '특별한 메뉴가 있어요': 'special menu',
          '가성비가 좋아요': 'good value', '커피가 맛있어요': 'good coffee', '디저트가 맛있어요': 'good desserts',
          '양이 많아요': 'large portions'}

def hbar(ax, x0, x1, yc, h_data, r_px, color, round_end=True):
    """Horizontal bar from x0 to x1 centred at yc; 4px-rounded data end, square at the baseline."""
    fig = ax.figure
    bbox = ax.get_window_extent()
    xl, yl = ax.get_xlim(), ax.get_ylim()
    xu = (xl[1] - xl[0]) / bbox.width      # data units per px
    yu = abs(yl[1] - yl[0]) / bbox.height
    rx, ry = min(r_px * xu, (x1 - x0) / 2), min(r_px * yu, h_data / 2)
    y0, y1 = yc - h_data / 2, yc + h_data / 2
    if not round_end or x1 - x0 <= 0:
        verts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
        codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    else:
        verts = [(x0, y0), (x1 - rx, y0), (x1, y0), (x1, y0 + ry), (x1, y1 - ry), (x1, y1), (x1 - rx, y1),
                 (x0, y1), (x0, y0)]
        codes = [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CURVE3, Path.CURVE3,
                 Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=color, edgecolor='none'))

def style_axis(ax, t):
    ax.set_facecolor(t['surface'])
    for s in ('top', 'right', 'bottom'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_color(t['base']); ax.spines['left'].set_linewidth(1)
    ax.tick_params(axis='y', length=0, colors=t['ink2'], labelsize=11)
    ax.tick_params(axis='x', length=0, colors=t['muted'], labelsize=10)
    ax.grid(axis='x', color=t['grid'], linewidth=1, linestyle='-')
    ax.set_axisbelow(True)

def render(df, mode, out_png):
    t = THEMES[mode]
    fig = plt.figure(figsize=(16, 6.4), dpi=100, facecolor=t['surface'])
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.05], wspace=0.42, left=0.14, right=0.97, top=0.80, bottom=0.10)
    # ---- panel A: venues per area group, stacked by type
    ax = fig.add_subplot(gs[0]); style_axis(ax, t)
    ct = pd.crosstab(df.iloc[:, 5], df.iloc[:, 3])
    order = ct.sum(axis=1).sort_values(ascending=True).index.tolist()
    ax.set_xlim(0, 135); ax.set_ylim(-0.6, len(order) - 0.4)
    ax.set_yticks(range(len(order))); ax.set_yticklabels([AREA_LABELS.get(a, a) for a in order])
    fig.canvas.draw()
    bbox = ax.get_window_extent(); yu = (len(order)) / bbox.height; xu = 135 / bbox.width
    h = 22 * yu; gap = 2 * xu
    for i, a in enumerate(order):
        m, d = int(ct.loc[a].get('식사', 0)), int(ct.loc[a].get('디저트', 0))
        if m: hbar(ax, 0, m, i, h, 4, t['s1'], round_end=(d == 0))
        if d: hbar(ax, m + (gap if m else 0), m + d, i, h, 4, t['s2'], round_end=True)
        ax.text(m + d + 2.2, i, f'{m + d}', va='center', ha='left', fontsize=11, color=t['ink'])
    ax.set_title('Venues per area group', loc='left', fontsize=14, color=t['ink'], pad=34, fontweight='bold')
    ax.text(0, 1.035, 'restaurant vs café/dessert split used to pair a meal with a café nearby', transform=ax.transAxes,
            fontsize=10.5, color=t['ink2'], va='bottom')
    handles = [plt.Rectangle((0, 0), 1, 1, color=t['s1']), plt.Rectangle((0, 0), 1, 1, color=t['s2'])]
    leg = ax.legend(handles, [f"식사 · restaurants ({int(ct.get('식사', pd.Series()).sum())})",
                              f"디저트 · cafés & desserts ({int(ct.get('디저트', pd.Series()).sum())})"],
                    loc='lower right', frameon=False, fontsize=10.5, handlelength=1.0, handleheight=1.0)
    for txt in leg.get_texts(): txt.set_color(t['ink2'])
    # ---- panel B: most frequent review keyword tags
    ax2 = fig.add_subplot(gs[1]); style_axis(ax2, t)
    tags = collections.Counter(x.strip() for s in df.iloc[:, 1].dropna() for x in str(s).split(','))
    top = tags.most_common(10)[::-1]
    xmax = 330
    ax2.set_xlim(0, xmax); ax2.set_ylim(-0.6, len(top) - 0.4)
    ax2.set_yticks(range(len(top))); ax2.set_yticklabels([f'{k}  ({TAG_EN.get(k, "")})' for k, _ in top])
    fig.canvas.draw()
    bbox = ax2.get_window_extent(); yu = len(top) / bbox.height
    h2 = min(18 * yu, 0.7)
    for i, (k, v) in enumerate(top):
        hbar(ax2, 0, v, i, h2, 4, t['s1'])
        ax2.text(v + 4, i, f'{v}', va='center', ha='left', fontsize=10.5, color=t['ink'])
    ax2.set_title('Most frequent review keyword tags', loc='left', fontsize=14, color=t['ink'], pad=34, fontweight='bold')
    ax2.text(0, 1.035, f'venues whose top-5 tags include the tag (of {len(df)} venues, {len(tags)} distinct tags)',
             transform=ax2.transAxes, fontsize=10.5, color=t['ink2'], va='bottom')
    fig.text(0.14, 0.955, f'Taste Trip venue set · {len(df)} venues around Mok-dong · Dangsan · Seonyudo, Seoul',
             fontsize=15.5, color=t['ink'], fontweight='bold')
    fig.text(0.97, 0.02, 'Source: data/Item_data.xlsx, jiheon branch (commit 23d8e10)', ha='right', fontsize=9,
             color=t['muted'])
    fig.savefig(out_png, facecolor=t['surface'])
    plt.close(fig)

if __name__ == '__main__':
    src, outdir = sys.argv[1], sys.argv[2]
    df = pd.read_excel(src)
    for mode in ('light', 'dark'):
        render(df, mode, os.path.join(outdir, f'dataset_overview_{mode}.png'))
        print('wrote', os.path.join(outdir, f'dataset_overview_{mode}.png'))
