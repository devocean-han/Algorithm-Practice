# 버블 정렬:
# 앞에서부터 두 수를 비교해서 자리바꾼다. 그렇게 끝까지 가면 제일 큰 수가 마지막에 오게 된다.
# 그 다음 또 앞에서부터 두 수를 비교해서 N-1자리까지 비교하면 그 다음 큰 수가 두 번째 마지막에 오게 되고,...

input = [4, 6, 2, 9, 1]

# 내 버전:
def bubble_sort1(array):
    for max_index in range(len(input), 1, -1):
        for index in range(1, max_index):
            if array[index - 1] > array[index]:
                temp = array[index]
                array[index] = array[index - 1]
                array[index - 1] = temp
    return array


# 강의판 버전:
def bubble_sort2(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

bubble_sort1(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

input2 = [4,7,2,3,6,9,1,8,5,0]
bubble_sort2(input2)
print(input2)