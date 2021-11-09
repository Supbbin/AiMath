from selenium import webdriver
import datetime
import pickle


def Timeday(기간):
    datelist=[]
    for i in range(기간):
        last_day = datetime.date.today() - datetime.timedelta(i)
        theday = str(last_day.year) + str(last_day.month) + str(last_day.day)
        datelist.append(theday)
    return datelist

wd = webdriver.Chrome('crawling1\chromedriver.exe')

news_title_list = []
for date in Timeday(3):
    for page_num in range(1):
        url = f'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date={date}&page={page_num}'
        wd.get(url)
        titles = wd.find_elements_by_xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt[2]/a')
        for title in titles:
            title = title.get_attribute("textContent").strip()
            news_title_list.append(title)
wd.quit()
print(news_title_list)


with open('ITnews.pkl', 'wb') as f:
    pickle.dump(news_title_list, f)


with open("ITnews.pkl", "rb") as fr:
    data = pickle.load(fr)
print(data)



# ##데이터 저장
# import pickle
# with open("data.pkl", "rb") as fr:




# def naver_news_tile(검색어, 검색개수):
#     page_num = 검색개수//10 + 1
#     wd = webdriver.Chrome('crawling1\chromedriver.exe')   #위의 옵션을 포함하여 웹드라이브를 실행함.
#     news_title_list = []
#     for i in range(page_num):
#         url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={}1'.format(검색어,page_num)
#         wd.get(url)
#         titles = wd.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[1]/section/div/div[2]/ul/li/div[1]/div/a')
#         for a in titles:
#             title = a.get_attribute('title')
#             news_title_list.append(title)
#     #news_title_list에 30개 담겨있는 상황
#     wd.quit()
#     return news_title_list[:검색개수]

# #다시 return 값을 담아줌

# result = naver_news_tile('방탄소년단', 27)
# # print(result)
# # print(len(result))
# # #len은 함수의 갯수