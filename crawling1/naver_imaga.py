from selenium import webdriver
import time
wd = webdriver.Chrome('crawling1\chromedriver.exe')

wd.get('https://naver.com')
wd.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=강아지')

## 현재 스크롤의 위치를 확인하여 prev_height에 담습니다. 
prev_height = wd.execute_script("return document.body.scrollHeight")

# 웹페이지 맨 아래까지 무한 스크롤
while True:
    # 스크롤을 화면 가장 아래로 내린다
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(2)
    # 현재 문서 높이를 가져와서 저장
    curr_height = wd.execute_script("return document.body.scrollHeight")
    if(curr_height == prev_height):   # 스크롤을 내렸음에도 이전 높이와 동일하다면 다 내린 것이기 때문에 break.
        break
    else:
        prev_height = wd.execute_script("return document.body.scrollHeight")