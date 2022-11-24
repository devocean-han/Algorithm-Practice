# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

numbers = [1, 1, 1, 1, 1]
target_number = 3


# 타겟 넘버를 반환해야 하는 줄 잘못 이해하고 품...
def get_count_of_ways_to_target_by_doing_plus_or_minus1(array, target):
    sum = numbers[0]
    for num in array[1:]:
        if sum < target:
            sum += num
        else:
            sum -= num
    return sum


# 하나씩 원소를 추가할 때마다
# 새로 추가된 원소를 더하고 빼는 경우의 수를 추가하면 됩니다.
numbers = [2, 3, 1]
target_number = 0
result = []  # 모든 경우의 수를 담기 위한 배열


# 강의판 '모든 경우의 수' 리스트에 저장하기:
def get_all_trees(array, current_index, current_sum, result):
    if current_index == len(array): # 탈출조건인데 음 왜 len(array) - 1이 아니지?
        result.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_trees(array, current_index + 1, current_sum + array[current_index], result)
    get_all_trees(array, current_index + 1, current_sum - array[current_index], result)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
# 모든 경우의 수가 출력됩니다!
# [6, 4, 0, -2, 2, 0, -4, -6]


# get_all_trees를 이용하여 target에 맞는 값 개수 반환:
def get_count_of_ways_to_target_by_doing_plus_or_minus2(array, target):
    possible_results = []
    get_all_trees(array, 0, 0, possible_results)
    print(possible_results)
    return possible_results.count(target)

print(get_count_of_ways_to_target_by_doing_plus_or_minus2(numbers, target_number))  # 5를 반환해야 합니다!
print(get_count_of_ways_to_target_by_doing_plus_or_minus2([1,1,1,1,1], 3))  # 5를 반환해야 합니다!
