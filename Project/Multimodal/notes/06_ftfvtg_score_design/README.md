# FTF-VTG design notes — post-processing and segment scoring (Score 정리)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../../README.md) › [Project](../../../README.md) › [Multimodal](../../README.md) › [Notes](../README.md) › **FTF-VTG design notes**</sub>

> [!NOTE]
> **Research working note (2025, in Korean)** — Working notes from the FTF-VTG research: an 8-hyper-parameter post-processing design (smoothing, derivative thresholds, decayed dynamic score, static/dynamic segment score, gap merging). The released code uses a later variant (hybrid morphological + first-order gradient with hysteresis thresholds). Kept in Jiheon Kang's track notes for the VTG research team; converted from Notion.

사용한 하이퍼 파라미터는 빨간색으로 색칠함. 총 8개 사용했다.

우리가 앞 단계에서 얻는 것은 프레임별 쿼리 유사도이다.

이를 통해서 우리는 구간을 추출할 것이다.

1. 가우시안 스무딩<br>- Stride(커널사이즈)를 정해서 가우시안 스무딩을 진행한다.<br>- sigma를 통해서 스무딩 강도를 지정한다.
2. 1차 미분값을 사용<br>- 1차 미분값이 0 이상과 0 이하인 값을 각각 정리한다. (즉 상승 부분과 하강 부분을 따로 모은다.)<br>- 각각 상승 부분과 하강 부분의 평균과 표준편차를 구한다.<br>- 평균 + $`\alpha`$\*표준편차를 통해서 임계값을 잡아 임계값을 넘을때를 이벤트의 시작과 끝 가능성을 보는 것.<br>- 알파를 통해 잡은 이유는 보다 유연한 대처를 위해서 평균과 표준편차를 사용함
3. 2차 미분값을 사용<br>- 2차 미분값은 local max와 local min을 찾을 수 있는 지표임.<br>- 이 근방의 값들에 가중치를 줌으로써 중요한 이벤트 부분을 강조하고, 아닌 부분을 배제할 수 있어서 사용.<br>- 이 부분도 하이퍼파라미터를 써도 좋을듯..?
4. 이전 프레임에 점수 비율 정도 반영<br>- 기존의 다이나믹 스코어는 단순히 합하는 형식이었지만, 과거의 정보는 점차 작게 유지하겠다는 의미에서 사용. 어디까지나 커지는 것을 방지하고 최근 정보를 민감히 받기 위해 사용<br>- beta를 이용함

여기까지하면 프레임별 다이나믹 스코어를 구했다.

이제 여기서 어떻게 구간을 추출하는지 보겠다.

1. 기울기가 양수에서 음수로 변하는 지점과 음수에서 양수로 변하는 지점을 이벤트의 시작과 끝 가능 지점으로 지정한다.
2. start points와 end points간의 조합을 통해서 다양한 구간을 생성한다.<br>- 단 이벤트라고 지정할 수 있는 최소한의 프레임 개수를 지정해준다. (b)
3. compute_segment_scores 함수를 통해 만들어진 새로운 static, dynamic 스코어를 일정 비율(a)로 더해준다. 이 점수가 새로운 구간의 점수가 된다.<br>- 여기서 말하는 static, dynamic 스코어는 위에 구한 프레임별 다이나믹스코어와는 완전히 다른 점수이다. 사실상 이부분은 논문의 스코어와 거의 유사하다고 봐야함. <br>- 특정 임계값 (delta)를 넘는 것만 모든 점수를 더해서 dynamic 스코어를 구함.<br>- 구간 내외 점수 차이를 static 스코어로 구함.<br>***사실 이 단계를 고친다면 가장 고쳐야할 듯 싶음.***
4. 구간별 새로운 점수에서 점수가 **0이하인 것**은 제외하고, 나머지 구간들 중에서 특정 프레임개수 이내의 이벤트들은 연속이라고 간주하고 합해서 다시 새로운 점수를 구해본다.<br>- 이전 구간의 끝과 이후 구간 시작이 gap_threshold의 개수 이내라면, 연속적인 이벤트라고 가정할 수 있다고 판단. 그래서 다양한 후보군을 만들고 그 속에서 다시 또 점수를 구한다.
5. 여기서 만들어지는 구간의 점수 중 가장 높은 점수가 추출이 된다.

---
<sub>[← CIR reading list](../05_cir_survey/README.md) · [🗒️ Notes index](../README.md) · [Multimodal track](../../README.md)</sub>
