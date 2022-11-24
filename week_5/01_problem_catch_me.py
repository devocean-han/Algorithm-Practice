# ✍️ 나 잡아 봐라
#
# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
#
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다
#
# 👏 여기서 잠깐! Tip
# 코딩테스트에서 큐를 사용할 때는
# collections.deque 를 사용하셔야 합니다.
# 성능 차이가 많이 나거든요..! 스택은 그대로 list 사용하셔도 됩니다.
# 따라서 앞으로는 큐가 필요할 때 다음과 같이 사용하겠습니다!
#
# >>> from collections import deque
# >>> queue = deque()
# >>> queue.append(3)
# >>> queue.append(4)
# >>> print(queue.popleft())
# 3

# => 일단 코니의 자취도 메모이제이션, 브라운의 '현재 위치' 기록도 메모이제이션 이용?


from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time_seconds = 0 # 1, 2, 3, ...., n, ... 631초까지 가능.
    queue = deque()
    queue.append((brown_loc, 0)) # 브라운의 위치를 시간과 함께 담아준다고 함.
        # 이것이 바로 메모이제이션?! 하지만 왜 시간과 함께여야 하는가...
        # BFS를 이용한다는데 왜 방문한 리스트 visited는 없는 것이며
        # 그래프나 트리의 값과 관계 도식인 인접 리스트 데이터도 없는데 어떻게 하지?

    # 위치를 인덱스로 가지는 리스트에 '방문 시간'을 음. 딕셔너리로 넣어준다.
    # 근데 딕셔너리가 빠르다지만 '해당 키가 있는지 없는지'를 검사하는 것과
    # 그냥 리스트에서 '해당 키가 있는지 없는지'를 검사하는 게 똑같이 걸리지 않을까?
    # 일단 'in 리스트'는 O(N)이 걸린다고 했는데. 딕셔너리에서 키의 유무를 검사하는 건 얼마나 걸리지?
    visited = [{} for _ in range(200001)]

    # 시간이 1초씩 지나갈 때마다~
    # 그만 두는 시점은 1. 코니가 200,000이상 지점으로 달렸을 때, 2. 잡혔을 때
    while cony_loc <= 200000:
        # 일단 코니 위치는 이전 위치 + 지난 시간(초)
        cony_loc += time_seconds
        if time_seconds in visited[cony_loc]:
            return time_seconds

        # 1초 지날 때마다 그 때의 queue 작업을 해줌...
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            # # 여기서 '방문 했냐'의 검사는, '코니를 잡았냐'의 검사로 대체하고
            # # 코니를 잡았다면 그냥 그 노드만 넘기고 지나가는 게 아니라 프로그램 전체를 종료한다.
            # if current_position == cony_loc and current_time == time_seconds:
            #     return current_time
            # => 처음에 'visited' 데이터 없이 그냥 queue와 이 탈출 조건으로 실행했을 때는 1,2번 케이스까지는 풀렸다.
            # => 3번이 실행이 오래 걸려서 중간에 끊었고. visited가 있고 없고의 차이가 뭐지?
            # => 또 전에 만든 BFS랑은 어떻게 이렇게 다르지? 뭐가 비슷한 부분이지?

            new_time = current_time + 1

            # 브라운도 조건이 있다: 위치 0~200,000을 벗어나면 안된다.
            new_position = current_position - 1
            if 0 <= new_position and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
                # 이미 그려진 인접 리스트가 없어도 그 때 그 때 가지 분기를 해나가는 식인 것 같다.
                # 즉, 그 때 그 때 그래프를 그리고, 당연히 새로 그려진 가지는 방문한 적이 없을 테니
                # 방문했는지 검사를 건너뛰고 그냥 바로 queue에 담기....?

            new_position = current_position + 1
            if new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time_seconds += 1

    return


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))


