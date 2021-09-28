
from datetime import datetime

# 카메라 동작중으로 while 문 안에 들어갈내용
## 카메라 동작은 수업 시작전 20분 전부터 수업 시작후 10분까지만 작동?
today_str = datetime.today().strftime('%Y년%m월%d일')
msg = f'{today_str}의 출결 정보입니다.\n'

member_dict = {0 : '수빈', 1 : '우석'}
while True:

    # 판독을해서 

    name = '수빈'  ## 머신이 추측한 이름을 변수로

    if name in member_dict.values(): 
        # 오늘 날짜와 시간 가져오기
        now_datetime = datetime.today()
        # 수업시작 시간 설정, 날짜 관계없음.
        start_time = datetime(now_datetime.year,now_datetime.month,now_datetime.day, hour = 11, minute=10)
        # 오늘 날짜만 가져오기 -> 엑셀에 날짜 입력해야 할거 같아서.
        today_date = now_datetime.date()
        # 오늘 시간만 가져오기 -> 실제 출석 시간이 될듯
        today_time = now_datetime.time()

        # 지각 시간 구하기 
        diff = now_datetime - start_time
        diff_min = diff.seconds/60       # 지각한 시간을 분으로 환산

        if diff.days <0:
            msg += f'{name}는 미리 도착하였습니다. 도착시간은 {today_time.strftime("%H시 %M분")}입니다.\n'
            print('수업 시작 전에 도착하였습니다.')

        elif diff_min<10:
            msg += f'{name}는 지각이 아닙니다. 도착시간은 {today_time.strftime("%H시 %M분")}입니다.\n'
    print(msg)
