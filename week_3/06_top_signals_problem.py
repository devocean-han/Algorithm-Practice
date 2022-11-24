## 스택 실전 사용법
# 위에서 스택을 구현해봤지만, 실제 코드에서는 파이썬의 list 를 이용해서 스택으로 사용합니다!
# 리스트의 .append()와 .pop()!!
#
# Q. 수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다.
# 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한 ,한 번 수신된 신호는 다른 탑으로
# 송신되지 않습니다.
#
# 이 때, 맨 왼쪽부터 순서대로 탑의 높이를 담은 배열 heights가 매개변수로 주어질 때 각 탑이 쏜
# 신호를 어느 탑에서 받았는지 기록한 배열을 반환하시오.
#
# [6, 9, 5, 7, 4] # 라고 입력된다면,
#
# # 아래 그림처럼 탑이 있다고 보시면 됩니다!
# <- <- <- <- <- 레이저의 방향
#    I
#    I
#    I     I
# I  I     I
# I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
#
# [0, 0, 2, 2, 4] # 다음과 같이 반환하시면 됩니다!


top_heights = [6, 9, 5, 7, 4]

# 내 버전 1: 시간 복잡도는 O(N^2)
# => 각 탑마다 왼쪽의 전체 탑과 비교하는 루프를 돌면서,
# => 자신보다 큰 탑의 번호를 적으면 된다.
# => 더 큰 탑이 없으면 0이고 자신이 가장 왼쪽의 탑이어도 0이다.
def get_receiver_top_orders1(heights):
    receive_tops = [0]
    for i in range(1, len(heights)): # i는 신호를 쏘아보낸 탑
        for j in range(i - 1, -1, -1):           # j는 신호를 받을 수 있는 후보 탑들
                 # (신호가 왼쪽으로 가기 때문에 뒤쪽(오른쪽) 탑부터 비교해야 함.)
            if heights[j] > heights[i]:
                receive_tops.append(j + 1)
                break
        else: # 후보 탑들을 다 둘러보도록 신호를 받지 못했으면
            receive_tops.append(0)
    return receive_tops


# 강의판 해답: 스택을 이용한다고 했지만 이러면 굳이 스택이라는 개념을 이용하는 의미가 없지 않나..?
# 게다가 탑들의 높이 데이터인 heights를 변경하게 되므로 더 안 좋은 것 같은데.ㅇㅇ
def get_receiver_top_orders2(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, -1, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders1(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
print(get_receiver_top_orders2(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders1([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders1([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders1([1,5,3,6,7,6,5]))

