class 학생성적():
    def __init__(self, name, korean, math):
        self.이름 = name
        self.국어 = korean
        self.수학 = math

    def 총점(self):
        return self.국어 + self.수학

    def 평균(self):
        return (self.국어 + self.수학)/2

    def 출력(self):
        print(self.이름 + self.총점(), self.평균(), sep='\t')

a = 학생성적('고아라', 82, 69)
a.출력
