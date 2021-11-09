#https://chromedriver.chromium.org/downloads

from selenium import webdriver

# wd = webdriver.Chrome('crawling1\chromedriver.exe') 
# #search_word = input('무엇을 검색하시겠습니까?')
# search_word = '방탄'
# url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'.format(search_word)

# wd.get(url) #웹페이지 접속

# #찾고 싶은 것
# titles = wd.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[1]/section/div/div[2]/ul/li/div[1]/div/a')

# ##정보를 가지고 오고 싶으면 wd.get_attribute
# title_list = [ ]

# for a in titles:
#     title = a.get_attribute('title')
#     title_list.append(title)

# print(title_list)
# wd.quit()



#30개를 리스트에 담아라.


def naver_news_tile(검색어, 검색개수):
    page_num = 검색개수//10 + 1
    wd = webdriver.Chrome('crawling1\chromedriver.exe')   #위의 옵션을 포함하여 웹드라이브를 실행함.
    
    news_title_list = []
    for i in range(page_num):
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={}1'.format(검색어,page_num)
        wd.get(url)
        titles = wd.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[1]/section/div/div[2]/ul/li/div[1]/div/a')
        for a in titles:
            title = a.get_attribute('title')
            news_title_list.append(title)

    #news_title_list에 30개 담겨있는 상황
    wd.quit()
    return news_title_list[:검색개수]

#다시 return 값을 담아줌

result = naver_news_tile('방탄소년단', 27)
# print(result)
# print(len(result))
# #len은 함수의 갯수


from PIL import Image
from wordcloud import WordCloud
import numpy as np

#갯수는 디폴트 값 설정
def make_wordcloud(주제어, 마스크, 갯수=30):
    '''마스크에는 ㅇㅇㅇ, ㅇㅇㅇ, ㅇㅇ가 있습니다.'''
    if 마스크 == 'ㅇㅇㅇ':
        path = ''
    elif 마스크 == 'ㅇㅇ':
        path = ' '
    elif 마스크 == 'ㅇ':
            

    # 이미지 마스크 만들기(꼭 png파일 필요합니다.) 
    # #워드 크라우드 마스크로 만들기 위해 행렬로 변환
    masks = np.array(Image.open('crawling1\worddd\png-clipart-cats-cats.png'))

    text = ""
    text_list = naver_news_tile('방탄소년단', 30)

    for title in text_list:
        text = text + ' ' + title


    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j]==5 or mask[i][j]==4:
                mask[i][j] = 255

    # 생성하기 ##뒤에 mask = mask 에서 뒷부분은 위에서 우리가 지정한 이름
    wc = WordCloud(font_path='crawling1\worddd\GmarketSansTTFBold.ttf', background_color="white", max_words=20000, mask=masks,max_font_size=300)
    wc.generate(text)
    
    # 파일 저장하기
    wc.to_file(f'{주제어}.png')