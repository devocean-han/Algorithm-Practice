# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은
# 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

# 예를 들어 S=0001100 일 때,
#
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
#
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


# => 전부를 0으로 뒤집을지, 1로 뒤집을지는 그냥 전체 수 중 더 많은 쪽으로 결정되지 않을까?
# => 하지만 100010001은 0이 더 많지만 1을 세 번 뒤집어 000000000으로 만들기보단 0들을 2번 뒤집어 111111111로 만들어야 한다.
# => 그냥 1에서 0으로 바뀌는 시점, 0에서 1로 바뀌는 시점이 몇 개나 되느냐를 세면 될 것 같은데..!
# => 아니 그냥 연속된 1이나 0들을 다 하나의 1이나 0으로 압축해서 더 많은 쪽으로 뒤집으면 되겠다.
# => 즉, 100010001 => 10101이 되어 1쪽으로 뒤집는 게 낫겠구나~를 알 수 있게 된다.
# => 오 그럼 남은 건 '뒤집어지는 쪽'의 개수만 반환하면 되는군! 즉, 뒤집어져야 하는 0이 2개니까 2를 반환하면 되겠다.

input = "011110"

# 실은 input을 0과 1로 압축시키는 문제!
# 0과 1이 새로 나올 때마다 리스트에 따로 넣어서 연이은 중복 제거한 방법:
def find_count_to_turn_out_to_all_zero_or_all_one1(string):
    new_string = [string[0]]
    for num in string[1:]:
        if new_string[-1] != num:
            new_string.append(num)
    new_string = ''.join(new_string)
    print(string)
    print(new_string)
    return min(new_string.count("1"), new_string.count("0"))

# 그냥 1->0으로, 0->1로 바뀌는 순간을 따로 카운트해서 비교한 방법:
def find_count_to_turn_out_to_all_zero_or_all_one2(string):
    zero_to_one = 0
    one_to_zero = 0
    if string[0] == "0":
        one_to_zero += 1
    else:
        zero_to_one += 1
    for index in range(1, len(string)):
        if string[index-1] != string[index]:
            if string[index] == "0":
                one_to_zero += 1
            else:
                zero_to_one += 1
    return min(zero_to_one, one_to_zero)

result = find_count_to_turn_out_to_all_zero_or_all_one2("1000011000101")
print(result)


# 정답 코드 (따로 보지 않음)(나와 로직은 거의 똑같다):
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)