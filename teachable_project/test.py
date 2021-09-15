
#-*- coding: utf-8 -*-

with open('teachable_project\labels.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

i = 0
for line in lines:
    print(line.strip().split(' ')) #스플릿의 공백으로 쪼개기


    # print(f'{i}번째 줄의 내용은 {line}입니다.')
    # i += 1