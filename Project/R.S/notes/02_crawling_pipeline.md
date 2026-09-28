# 웹 크롤링 코드 짜기 및 심화 공부 — 가게 → 리뷰 → 리뷰어 3단계 파이프라인

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [R.S](../README.md) › [Notes](README.md) › **Crawling pipeline**</sub>

> [!NOTE]
> Jiheon's personal study note (deep daiv. WIL) written during the Taste Trip recommender project, kept in the original Korean.

프로젝트를 위해 처음 시작한 웹 크롤링 공부와 어떻게 코드를 짜야할지 고민하고 다양한 코딩 실력을 키우기

현재까지 프로젝트를 위해 작성했던 코드는

1. 지역을 정하면 해당 가게 URL 크롤링
2. 가게 리뷰에서 리뷰와 리뷰자 크롤링
3. 리뷰자의 리뷰주소에 들어가서 리뷰들 모두 크롤링

이렇게 각각 코드를 구현했었다.

이 코드들을 어떻게 하나로 붙여서 편하게 코드를 구현할지 고민해야한다.

먼저 엑셀 파일로 만들어진 파일을 어떻게 불러오는지 알아보았다.

```python
file_path = 'Place_Info_final.xlsx'
sheet_name = 'output'   # 엑셀 파일의 경로

# 엑셀 파일을 읽습니다.
df = pd.read_excel(file_path, sheet_name = sheet_name)

column_data = df.iloc[:, [0, 2]].values.tolist()
```

이런 식으로 경로와 시트의 이름을 지정해주면 엑셀 파일을 열 수 있었다. 그리고 .iloc를 이용하면 특정 열이나 행의 값들을 받아올 수 있다.

또한 selenium을 이용한 webdriver에서 find_element와 find_elements 차이를 알게 되었고 더욱 유용하게 코드를 짤 수 있었다.

find_element는 찾으면 스트링 형태로 변환하고, 만약 비어있다면 에러코드가 난다.

find_elements는 말그대로 있는 모든 요소를 다 찾기 때문에 있으면 리스트로 쭉 변환하고, 만약 없다면 빈 리스트가 나오게 된다.

그래서 if문으로 예외 사항을 처리하기는 find_elements가 적합하고, 하나로 분명히 정해진 것이라면 find_element로 text를 받는 것이 더 효율적인 것을 알 수 있었다.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
from openpyxl import Workbook
import datetime
import time
import re

options = Options()
options.add_argument("window-size=1920x1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://m.place.naver.com/restaurant/list?query=%EA%B0%95%EB%82%A8%EB%A7%9B%EC%A7%91&x=129.1592254&y=35.1630911&entry=pll&keywordFilter=filterOpening%5Etrue&level=top")
driver.implicitly_wait(10)

now = datetime.datetime.now()
xlsx = Workbook()
list_sheet = xlsx.create_sheet('output')
list_sheet.append(['Name', 'Reviews', 'URL'])

time.sleep(50)

try:
    place = driver.find_elements(By.CSS_SELECTOR, 'li.UEzoS')

    for p in place:
        Name = p.find_element(By.CSS_SELECTOR, 'div.N_KDL').text.strip()
        Reviews_elements = p.find_element(By.CSS_SELECTOR, 'div.MVx6e').text.strip()
        Reviews = str(Reviews_elements)
        Reviews_list = re.findall(r'\d+', Reviews_elements)
        if Reviews_list:
            Reviews = Reviews_list[0]  # This takes the first number found, assuming it's the count of reviews
            Reviews = int(Reviews)  # Convert to integer if needed
        else:
            Reviews = 0 
        URL = p.find_element(By.CSS_SELECTOR, 'a[href*="/restaurant"]').get_attribute('href')

        #리뷰수가 300 이상이라는 조건문 추가
        if Reviews > 100:
            list_sheet.append([Name, Reviews, URL])

except Exception as e:
    print('Error:', e)
finally:
    # Excel 파일 저장 및 드라이버 종료
    file_name = 'Place_Info_final.xlsx'
    xlsx.save(file_name)
    driver.quit()

print("Data collection completed and saved to Excel.")

time.sleep(3)

# 엑셀 파일 경로와 열 이름을 지정합니다.
file_path = 'Place_Info_final.xlsx'
sheet_name = 'output'   # 엑셀 파일의 경로

# 엑셀 파일을 읽습니다.
df = pd.read_excel(file_path, sheet_name = sheet_name)

print(df.head())          # 첫 몇 행을 출력
print(df.shape) 

# 특정 열의 정보를 리스트로 가져옵니다.
column_data = df.iloc[:, [0, 2]].values.tolist()

xlsx = Workbook()
list_sheet = xlsx.create_sheet('output')
list_sheet.append(['Name', 'URL'])

try:
    for c in column_data:
        P_Name = c[0]
        URL_num = re.findall(r'restaurant/(\d+)', c[1])
        URL_num = str(URL_num)
        URL_num = URL_num.replace("[", '')
        URL_num = URL_num.replace("]", '')
        URL_num = URL_num.replace("'", '')
        URL_rev = "https://m.place.naver.com/restaurant/" + URL_num + "/review/visitor?entry=pll&reviewSort=recent"
        list_sheet.append([P_Name, URL_rev])

except Exception as e:
    print('Error:', e)
finally:
    # Excel 파일 저장 및 드라이버 종료
    file_name = 'Place_URL_final.xlsx'
    xlsx.save(file_name)
    driver.quit()

```

가게 URL을 받을 수 있는 코드이다. 엑셀에 리뷰창이 바로 뜰 수 있도록 주소를 저장한다.

```python
file_path = 'Place_URL_final.xlsx'
sheet_name = 'output'   # 엑셀 파일의 경로

# 엑셀 파일을 읽습니다.
df = pd.read_excel(file_path, sheet_name = sheet_name)

print(df.head())          # 첫 몇 행을 출력
print(df.shape) 
Place_data = df.iloc[:, [0, 1]].values.tolist()

xlsx = Workbook()
list_sheet = xlsx.create_sheet('output')
list_sheet.append(['Name', 'URL'])

now = datetime.datetime.now()
xlsx = Workbook()
list_sheet = xlsx.create_sheet('output')
list_sheet.append(['Name', 'nickname', 'content', 'date', 'revisit', 'tags', 'review_cnt', 'url'])

for p in Place_data:
    place_name = p[0]
    place_URL = p[1]
    driver.get(place_URL)
    driver.implicitly_wait(10)

# 전체 더보기 버튼 클릭하여 모든 리뷰 로드
    try:
        while True:
            try:
                more_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.fvwqf'))
                )
                driver.execute_script("arguments[0].click();", more_button)
                time.sleep(3)  # 새로운 리뷰 로드 대기
            except Exception as e:
                print("No more pages to load:", e)
                break

    # 모든 페이지가 로드되었으므로, 이제 리뷰 데이터와 태그를 수집
        reviews = driver.find_elements(By.CSS_SELECTOR, 'li.pui__X35jYm.EjjAW')

        for r in reviews:
            nickname = r.find_element(By.CSS_SELECTOR, 'span.pui__uslU0d').text.strip()
            content = r.find_element(By.CSS_SELECTOR, 'div.pui__vn15t2').text.strip()
            date = r.find_element(By.CSS_SELECTOR, 'span.pui__gfuUIT > time').text.strip()
            revisit_elements = r.find_elements(By.CSS_SELECTOR, 'span.pui__gfuUIT')
            revisit = revisit_elements[1].text.strip() if len(revisit_elements) > 1 else ''
            review_cnt = r.find_element(By.CSS_SELECTOR, 'span.pui__WN-kAf').text.strip()
            url = r.find_element(By.CSS_SELECTOR, 'a[href*="/my"]').get_attribute('href')

        # revisit "번째 방문" 문자 제거
            if revisit:
                revisit = int(revisit[:-5])
        
        # review_cnt "리뷰 " 문자 제거
            if review_cnt:
                review_cnt = int(review_cnt[3:])

        # 태그 더보기 클릭
            i_tags = [tag.text.strip() for tag in r.find_elements(By.CSS_SELECTOR, 'div.pui__HLNvmI')]
            i_tags = str(i_tags)
            if "+" not in i_tags:
                i_tag = [tag.text.strip() for tag in r.find_elements(By.CSS_SELECTOR, 'div.pui__HLNvmI')]
            else:
                tag_button = r.find_element(By.CSS_SELECTOR, 'a.pui__jhpEyP.pui__ggzZJ8')
                driver.execute_script("arguments[0].click();", tag_button)
                time.sleep(1)
                i_tag = [tag.text.strip() for tag in r.find_elements(By.CSS_SELECTOR, 'div.pui__HLNvmI span.pui__jhpEyP')]

            if review_cnt > 200:
                list_sheet.append([place_name, nickname, content, date, revisit, ", ".join(i_tag), review_cnt, url])
        
    except Exception as e:
        print('Error:', e)

        # Excel 파일 저장 및 드라이버 종료
file_name = f'naver_review_preview.xlsx'
xlsx.save(file_name)
driver.quit()

print("Data collection completed and saved to Excel.")

```

가게 별로 리뷰를 모으고 리뷰자의 이름과 URL을 받아온다.

이를 엑셀 파일로 저장하고 밑의 코드에서 받을 수 있도록 한다.

```python
file_path = 'naver_review_preview.xlsx'
sheet_name = 'output'   # 엑셀 파일의 경로

# 엑셀 파일을 읽습니다.
df = pd.read_excel(file_path, sheet_name = sheet_name)

print(df.head())         
print(df.shape) 
User_data = df.iloc[:, [0, 1, 7]].values.tolist()

xlsx = Workbook()
list_sheet = xlsx.create_sheet('output')
list_sheet.append(['nickname', 'name','category', 'review', 'date', 'tags', 'numbers', 'OX'])

for u in User_data:
    user_origin = u[0] 
    user_nickname = u[1]
    user_URL = u[2]

    driver.get(user_URL)
    driver.implicitly_wait(10)

    photo_video_review_checkbox = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, 'onlyHasMedia'))
    )
    # 체크되어 있다면 클릭해서 해제
    if photo_video_review_checkbox.is_selected():
        driver.execute_script("arguments[0].click();", photo_video_review_checkbox)
    time.sleep(2)  # 잠시 대기하여 상태가 반영되도록 함
    
    first_post = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._5RYLm7.bEchjN'))
            )

    driver.execute_script("arguments[0].click();", first_post)
    time.sleep(5) 

    for i in range(0,50):
        for c in range(0,20):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    try:
        nickname = driver.find_element(By.CSS_SELECTOR, 'h1._3q8NFd').text.strip()
        if nickname != u[1]:
            "something goes wrong! you should do it well!! hahahaha"

        stores = driver.find_elements(By.CSS_SELECTOR, 'div._898uc8')

        for s in stores:
            store_name = s.find_element(By.CSS_SELECTOR, 'span.pui__pv1E2a').text.strip()

            i_store_category = s.find_elements(By.CSS_SELECTOR, 'div.pui__Vb-OW1')

            if i_store_category and not i_store_category[0].text.strip():
                store_category = "없음"
            elif any("폐업" in element.text for element in i_store_category):
                store_category = "폐업했거나 정보 제공이 중지된 장소"
            else:
                store_category = s.find_element(By.CSS_SELECTOR, 'span.pui__WUm6H8').text.strip()

            store_review = s.find_element(By.CSS_SELECTOR, 'div.pui__vn15t2').text.strip()

        # 방문일\n7.28.일\n년 7월 28일 일요일 으로 뜨는 것을 수정해야함
            i_store_date = s.find_element(By.CSS_SELECTOR, 'span.pui__gfuUIT').text.strip()
            line = i_store_date.split('\n')
            store_date = line[-2]

            revisit_elements = s.find_elements(By.CSS_SELECTOR, 'span.pui__gfuUIT')
            revisit = revisit_elements[1].text.strip() if len(revisit_elements) > 1 else ''

        # revisit "번째 방문" 문자 제거
            if revisit:
                revisit = int(revisit[:-5])

            i_tags = [tag.text.strip() for tag in s.find_elements(By.CSS_SELECTOR, 'div.pui__HLNvmI')]
            i_tags = str(i_tags)
            if "+" not in i_tags:
                i_tag = [tag.text.strip() for tag in s.find_elements(By.CSS_SELECTOR, 'div.pui__HLNvmI span.pui__jhpEyP')]
            else:
                tag_button = s.find_element(By.CSS_SELECTOR, 'a.pui__jhpEyP.pui__ggzZJ8')
                driver.execute_script("arguments[0].click();", tag_button)
                time.sleep(1)
                i_tag = [tag.text.strip() for tag in s.find_elements(By.CSS_SELECTOR, 'div.pui__HLNvmI span.pui__jhpEyP')]
            
            if store_name == u[0]:
                OX = "O"
            else:
                OX = "X"

            list_sheet.append([nickname, store_name, store_category, store_review, store_date,  ", ".join(i_tag), revisit, OX])

    except Exception as e:
        print('Error:', e)

    
    # Excel 파일 저장 및 드라이버 종료
file_name = f'Reviewer_{now.strftime("%Y-%m-%d_%H-%M-%S")}.xlsx'
xlsx.save(file_name)
driver.quit()

print("Data collection completed and saved to Excel.")
```

각각 리뷰자마다 리뷰들을 받아서 쭉 나열한다.

---
<sub>[← Notes index](README.md) · [🍜 Taste Trip project](../README.md)</sub>
