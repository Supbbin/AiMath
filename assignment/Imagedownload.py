from selenium import webdriver
import requests
import time 
import os

keyword = input('어떤 이미지를 다운로드 받고 싶으신가요?')
want_num = int(input('몇 장의 이미지를 다운로드 받고 싶으신가요?'))

wd = webdriver.Chrome('crawling1\chromedriver.exe')

wd.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword))
print(f'이미지 검색에서 {keyword}를 검색하였습니다.')

img_folder = f'./{keyword}_img'     
if not os.path.isdir(img_folder) : # 없으면 새로 생성하는 조건문 
    os.mkdir(img_folder)


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





i = 1
for image in images:
    if i == want_num:
        break
    try:
        url = image.get_attribute('src')
        img_data = requests.get(url).content
        with open(img_folder + '/' + f'img{i}.jpg', 'wb') as img:
            img.write(img_data)
        
        if i == len(images):
            break
        i += 1
    except:
        print('실패했습니다')
        pass
if i < want_num:
    wd.get("https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj6z-zAzM3yAhXHVt4KHcxJCCcQ_AUoAXoECAEQAw&biw=1920&bih=925".format(keyword))
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
        imagess = wd.find_elements_by_xpath('//*[@id="islrg"]/div[1]/div/a[1]/div[1]/img')
        

    for imagen in imagess:
        try:
            url = imagen.get_attribute('src')
            img_dataa = requests.get(url).content
            with open(img_folder + '/' + f'img구글{i}.jpg', 'wb') as imgg:
                imgg.write(img_dataa)
            
            if i == want_num:
                break
            i += 1
        except:
            print('실패했습니다')
            pass
wd.quit()
