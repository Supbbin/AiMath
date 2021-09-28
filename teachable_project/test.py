
#-*- coding: utf-8 -*-

def make_dict(file_path):
    '''file_path는 텍스트 파일의 경로를 지정해주세요'''
    with open(file_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    image_dict = {}

    for line in lines:
        words = (line.strip().split(' ')) #스플릿의 공백으로 쪼개기
        index = words[0]
        keyword = words[1]
        image_dict[index] = keyword

    return image_dict

if __name__ == '__main__' :
#단독으로 실행시킬 때에 실행될 수 있는 명령어
    print(make_dict('C:/Users/수빈/Desktop/인공지능 수학/teachable_project/labels.txt'))