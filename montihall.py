import random

def monti(시도, 문):        # 시도는 시도 횟수, 문은 문의 갯수(만약 3이면 기본 몬티홀 문제)
    first_select = 0          # 선택을 바꾸지 않았을 때 상품을 타는 횟수를 카운트 하는 거
    change_select = 0         # 선택을 바꿨을 때 상품을 타는 횟수를 카운트 하는 거
    for i in range(시도):
        car = random.randint(1, 문)        # 1부터 문의 개수까지의 수 중 정수를 랜덤하게 뽑아서 그걸 자동차로 지정.
                                              # 리스트와 달리 른쪽 숫자 포함됨, 즉 미만이 아닌 이하.
        num_list = list(range(1,문+1))      # 문의 개수만큼 숫자를 만들어 이중에 선택하게 만들려고 함. 리스트는 미만이라 문+1
        first_select_num = random.randint(1,문)    # 처음 선택한 숫자를 랜덤으로 고름.
        if first_select_num == car:                 # 만약 그 숫자가 당첨숫자와 같다면
            first_select += 1                        # 선택을 바꾸지 않았을 때의 수를 하나 올림.
    #### 선택을 바꿨을 경우
        else:
            # 본인이 선택한 숫자와 실제 상품의 숫자를 제외하고 하나를 보여줘야 하므로
            num_list.remove(first_select_num)      # 본인이 선택한 숫자를 방 번호 리스트에서 삭제함.
            num_list.remove(car)                  # 차 숫자를 방 번호 리스트에서 삭제함.
            open_num = random.choice(num_list)     # 사회자가 보여주는 숫자를 선택함.
            num_list.remove(open_num)              # 사회자가 보여준 숫자를 삭제함.
            num_list.append(car)                  # 차 숫자를 방 번호에 다시 추가함.
            change_select_num = random.choice(num_list)    # 이렇게 된 숫자리스트에서 변경된 숫자를 하나 뽑음.
            if change_select_num == car:       # 만약 같으면 선택을 바꿧을 때 당첨되는 카운트를 하나 늘림.
                change_select += 1
    # for문 다돌고 나서 프린트함. \n 은 엔터예요^^.
    print(str(문) + "개의 문 중 하나의 차가 있다.\n" + str(시도) + "번 시도한 후 선택을 유지한 경우와 바꾼 경우의 확률은 다음과 같다.\n"
         + "선택을 유지한 경우 확률은 " + str(first_select/시도) + "\n선택을 변경한 경우 확률은 " + str(change_select/시도))



#### 갯수 설정
monti(10000,3)