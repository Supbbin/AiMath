# a = ['김샛별', 63+59, 63+59/2]
# b = ['기나영', 188, 94]
# c = ['박철수', 134, 67]
# d = ['고아라', 151, 75.5]
# e = ['최민수', 190, 95]

# i = [a, b, c, d, e]

# print('이름', '총점', '평균')
# for n in i:
#     print(n)



#NEw


def 학생_생성(name, korean, math):
    return {'이름' : name, '국어' : korean, '수학': math}

students = [
    학생_생성('김샛별', 63, 59),
    학생_생성('기나영', 89, 99),
    학생_생성('박철수', 67, 67),
    학생_생성('고아라', 82, 69),
    학생_생성('최민수', 93, 97),
]


def 총점(student):
    return student['국어'] + student['수학']

def 평균(student):
    return (student['국어'] + student['수학']) / 2

def 출력(student):
    print(student['이름'], 총점(student), 평균(student), sep='\t')


for student in students:
    출력(student)