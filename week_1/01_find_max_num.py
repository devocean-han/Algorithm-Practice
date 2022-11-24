print('hello')

# 최댓값 찾기 방법 3가지
input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max = array[0]
    for num in array:
        if max < num:
            max = num
    return max


def find_max_num2(array):
    return sorted(array)[-1]


def find_max_num3(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
print(find_max_num2(input))
print(find_max_num3(input))
