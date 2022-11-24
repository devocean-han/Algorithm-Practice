# Q3. ✍️ CGV 극장 좌석 자리 구하기
#
# Q. 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다.
# 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다.
#
# 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
#
# 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고,
# 6번 좌석이나 8번 좌석에도 앉을 수 있다.
# 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.
#
# 그런데 이 극장에는 “VIP 회원”들이 있다.
# 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.
#
# 예를 들어서,
# 그림과 같이 좌석이 9개이고,
# 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다.
# 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.
#
# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# 총 좌석의 개수와 VIP 회원들의 좌석 번호들이 주어졌을 때,
# 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 반환하시오.
#
# (그림 참고:
# https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F08798d1e-2853-4d8b-a877-f50f76df4159%2FUntitled.png?table=block&id=1b27b575-2457-41a0-ac3b-9201232882b2&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=650&userId=87c3dcfe-4739-463c-b420-d25b653a6ccb&cache=v2)

# => 가짓수를 모두 순회하는 건 그 때 더하기 빼기조합 구할 때 재귀로 했던 것처럼 할 수 있을 것 같은데.
# => 그냥 전체 자리 배치 조합 수에서 '안 되는 조합'의 수를 빼면 되지 않을까?
# =>

seat_count = 9
vip_seat_array = [4, 7]


# 가능한 모든 자리배치 조합을 구하기 (VIP 제외ㅠㅠ):
def get_all_trees1(N, current_seat, current_placement, was_swapped, result):
    # 마지막 좌석을 배정할 순서가 된다면, 그냥 그대로 배정하고 저장!
    # 아, 스왑되어 와서 마지막 좌석번호가 아닐 수도 있다....
    # 그냥 current_placement의 길이가 N-1이면~ 이라고 하자...
    if len(current_placement) == (N - 1):
        current_placement.append(current_seat)
        # current_placement += str(current_seat)
        result.append(current_placement)
        return

    ###########
    # 세 가지 분기 전에, VIP 자리로 두 가지 분기:
    # '내 앞'좌석이 VIP라면: 스왑 루트 불가능. 무조건 비스왑으로만 가야 한다.
    #           즉, 1, 2번 분기로만 진행이 가능하다.
    # '내'가 VIP 좌석이라면: 역시나 비스왑으로만 가야 한다. 그런데 이 경우엔
    #           비스왑으로부터 도착했다는 조건이 추가되었을 것이므로, 자동으로 2번 분기행!
    # => 즉 '내 앞' 좌석이 VIP면 3번 봉쇄(해야함). '내'가 VIP면 3번 봉쇄(해야함)에, 1번은 자동으로 봉쇄됨.
    ###########

    # 세 가지 분기:
    # 1. 스왑 루트를 타고 왔다 => 비스왑 루트로 간다:
    # ('내 앞' 좌석이 VIP라면 3번만 봉쇄하면 됨 => 따로 처리할 필요 없음) (어차피 비스왑 루트로 가고 있으므로)
    # ('내'가 VIP석이라면 3번을 봉쇄해야 하고 1번은 자동으로 봉쇄됨)
    #       (이 전에 비스왑 루트를 통해 도착했을 것이므로 어차피 이 1번 분기에 해당하지 않는다)
    if was_swapped:
        current_placement.append(current_seat)
        # current_placement += str(current_seat)
        get_all_trees1(N, current_seat + 2, current_placement[:], False, result)
    else:
        # 2. 비스왑 루트를 타고 왔다 => 비스왑 루트로 간다: ('내 앞'이나 '내'가 VIP석이라면 이쪽만 가능)
        current_placement.append(current_seat)
        # current_placement += str(current_seat)
        get_all_trees1(N,  current_seat + 1, current_placement[:], False, result)

        # 3. 비스왑 루트를 타고 왔다 => 스왑 루트로 간다:
        # ('내 앞'과 '내'가 VIP석인 경우 이쪽을 봉쇄해야 한다.)
        # (즉, 이쪽 분기는 '나'와 '내 앞'이 VIP가 아닌 경우에만 가능)
        # if current_seat not in vips and current_seat + 1 not in vips:
        current_placement.pop()
        current_placement.append(current_seat + 1)
        # current_placement = current_placement[:-1]
        # current_placement += str(current_seat + 1)
        get_all_trees1(N, current_seat, current_placement[:], True, result)


# 가능한 모든 자리배치 조합을 구하기:
def get_all_trees2(N, vips, current_seat, current_placement, was_swapped, result):
    # 마지막 좌석을 배정할 순서가 된다면, 그냥 그대로 배정하고 저장!
    # 아, 스왑되어 와서 마지막 좌석번호가 아닐 수도 있다....
    # 그냥 current_placement의 길이가 N-1이면~ 이라고 하자...
    if len(current_placement) == (N - 1):
        current_placement.append(current_seat)
        # current_placement += str(current_seat)
        result.append(current_placement)
        return

    ###########
    # 세 가지 분기 전에, VIP 자리로 두 가지 분기:
    # '내 앞'좌석이 VIP라면: 스왑 루트 불가능. 무조건 비스왑으로만 가야 한다.
    #           즉, 1, 2번 분기로만 진행이 가능하다.
    # '내'가 VIP 좌석이라면: 역시나 비스왑으로만 가야 한다. 그런데 이 경우엔
    #           비스왑으로부터 도착했다는 조건이 추가되었을 것이므로, 자동으로 2번 분기행!
    # => 즉 '내 앞' 좌석이 VIP면 3번 봉쇄(해야함). '내'가 VIP면 3번 봉쇄(해야함)에, 1번은 자동으로 봉쇄됨.
    ###########

    # 세 가지 분기:
    # 1. 스왑 루트를 타고 왔다 => 비스왑 루트로 간다:
    # ('내 앞' 좌석이 VIP라면 3번만 봉쇄하면 됨 => 따로 처리할 필요 없음) (어차피 비스왑 루트로 가고 있으므로)
    # ('내'가 VIP석이라면 3번을 봉쇄해야 하고 1번은 자동으로 봉쇄됨)
    #       (이 전에 비스왑 루트를 통해 도착했을 것이므로 어차피 이 1번 분기에 해당하지 않는다)
    if was_swapped:
        current_placement.append(current_seat)
        # current_placement += str(current_seat)
        get_all_trees2(N, vips, current_seat + 2, current_placement[:], False, result)
    else:
        # 2. 비스왑 루트를 타고 왔다 => 비스왑 루트로 간다: ('내 앞'이나 '내'가 VIP석이라면 이쪽만 가능)
        current_placement.append(current_seat)
        # current_placement += str(current_seat)
        get_all_trees2(N, vips, current_seat + 1, current_placement[:], False, result)

        # 3. 비스왑 루트를 타고 왔다 => 스왑 루트로 간다:
        # ('내 앞'과 '내'가 VIP석인 경우 이쪽을 봉쇄해야 한다.)
        # (즉, 이쪽 분기는 '나'와 '내 앞'이 VIP가 아닌 경우에만 가능)
        if (current_seat not in vips) and (current_seat + 1 not in vips):
            current_placement.pop()
            current_placement.append(current_seat + 1)
            # current_placement = current_placement[:-1]
            # current_placement += str(current_seat + 1)
            get_all_trees2(N, vips, current_seat, current_placement[:], True, result)


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    # get_all_tress 호출법:
    possible_results = []
    # get_all_trees1(5, 1, [], False, possible_results)  # []를 넘겨줘도 잘 될까? => 안 된다. list.append()는 배열을 반환하는 게 아니라서.
            # str은 str += str(좌석번호) 했을 때 새 str이 만들어져서 '분기'가 가능한 거지만 리스트는 하나의 current_placement에 계속 더하고 빼게 되므로 안된다.
            # '더하고' '뺄' 때 새 객체가 만들어져 반환되되 각 숫자(좌석번호)를 분리된 수로 보관할 수 있는 데이터 타입을 찾자.
            # str은 숫자 10을 넘어가는 순간 고장난다.
            # 튜플? 튜플밖에 없는데 일단은.. => 튜플이 순서 보존 되는가? 더하고 빼는 메소드가 새 객체를 반환하는가?
            # 진짜 정 안되면 좌석이 더해질때마다 ... 안되겟다. 112가 1과 12인지 11과 2인지 구분하기가 어렵겠다.
            # 튜플... 네가 희망이다..!
            # 잠깐만... 리스트가 왜 안되지..? ... ...
            # 고쳤다아아!! 같은 리스트를 자꾸 참조해서 문제라면 '복사해서' 새 리스트를 넘겨주면 되는 문제였어..!! 흐어어ㅇ러라미ㅣㅏㅏㅠㅠ
    get_all_trees2(total_count, fixed_seat_array, 1, [], False, possible_results)  # []를 넘겨줘도 잘 될까? => 안 된다... => 된다! 재귀 호출시 [:]를 넘기면 된다.
    print()
    for result in possible_results:
        print(result)

    # 잠깐만... VIP 고려하지 않고 받아온 저 결과 배치 중에서 VIP가 VIP석에 앉아 있지 않은
    # 경우만 빼면 되는 거잖아...? 머리 아프게 get_all_trees에 다 떼려넣지 않고..!
    # => 아니다 이게 더 복잡하다... 사실 깊게 생각해보지 않았다. 그냥 get_all_trees에 구현이 가능했다. 생각보다 간단하게..!
    return len(possible_results)


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print()
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))
# print(get_all_ways_of_theater_seat(30, [3, 10, 25, 29])) # 27580개 ㄷㄷ
# print(get_all_ways_of_theater_seat(30, range(10, 21))) # 4895개




