
# 곱하기 혹은 더하기를 순차적으로 계산하여 최대의 결과값이 나오도록 만들기
# 주어지는 수들은 0 혹은 양수이다.
# => 0이나 1일 때 더하기, 나머지는 곱하기를 하면 될 것 같은데.
# => 이전까지의 결과값이 0인 경우도 더하기를 해줘야 한다.
# => (강의에서 짚은 팁!) 이전까지의 결과값이 1인 경우도 더하기를 해줘야 한다!
#   왜냐면 1*2보다 1+2가, 1*3보다 1+3이... 항상 더 큰 결과를 낼 것이므로.

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result = array[0]
    for num in array[1:]:
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    return result


result = find_max_plus_or_multiply(input)
print(result)