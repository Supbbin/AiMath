
from PIL import Image
from wordcloud import WordCloud
import numpy as np

# 이미지 마스크 만들기(꼭 png파일 필요합니다.) 
# #워드 크라우드 마스크로 만들기 위해 행렬로 변환
mask = np.array(Image.open('crawling1\worddd\png-clipart-cats-cats.png'))



text = ""
text_list = naver_news_tile('방탄소년단', 30)

for title in text_list:
    text = text + ' ' + title


for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j]==5 or mask[i][j]==4:
            mask[i][j] = 255

# print(mask)
# 생성하기 ##뒤에 mask = mask 에서 뒷부분은 위에서 우리가 지정한 이름
wc = WordCloud(font_path='crawling1\worddd\GmarketSansTTFBold.ttf', background_color="white", max_words=20000, mask=mask,max_font_size=300)
wc.generate(text)
# 파일 저장하기
wc.to_file('worddd.png')
