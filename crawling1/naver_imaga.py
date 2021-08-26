from selenium import webdriver
import requests
import time 
 
keyword = input('어떤 이미지를 다운로드 받고 싶으신가요?')
# want_num = int(input('몇 장의 이미지를 다운로드 받고 싶으신가요?'))

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # 창을 띄우지 않고 실행
wd = webdriver.Chrome('crawling1\chromedriver.exe')   #위의 옵션을 포함하여 웹드라이브를 실행함.
wd.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword))
print(f'네이버 이미지 검색에서 {keyword}를 검색하였습니다.')

time.sleep(3)


prev_height = wd.execute_script("return document.body.scrollHeight")
while True:
    # 스크롤을 화면 가장 아래로 내린다
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(2)
    # 현재 문서 높이를 가져와서 저장
    curr_height = wd.execute_script("return document.body.scrollHeight")
    print('스크롤을 내리고 있습니다. 잠시 기다려 주세요.')
    if(curr_height == prev_height):
        break
    else:
        prev_height = wd.execute_script("return document.body.scrollHeight")





images = wd.find_elements_by_xpath('//*[@id="main_pack"]/section/div/div[1]/div[1]/div/div/div[1]/a/img')

print(images)

i = 0
for image in images:
    try:
        url = image.get_attribute('src')
        img_data = requests.get(url).content
        with open(f'img{i}.jpg', 'wb') as img:
            img.write(img_data)
        i += 1
    except:
        print('실패했습니다')
        pass

