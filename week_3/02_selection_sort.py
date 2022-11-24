# 선택 정렬:
# 최솟값을 가장 앞으로 가져오고, 그 다음 수부터 검사해서 다음 최솟값을 두 번째 자리로 가져오고,...

input = [4, 6, 2, 9, 1]
input2 = [4,7,2,3,6,9,1,8,5,0]

def selection_sort1(array):
    for j in range(len(array) - 1): # 비교할 첫자리를 좁혀주는 j
        current_min_index = j
        for i in range(j, len(array)): # j부터 끝까지 비교
            if array[current_min_index] > array[i]:
                current_min_index = i
        array[j], array[current_min_index] = array[current_min_index], array[j]
    return array


selection_sort1(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


# 강의판 버전:
def selection_sort2(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]
    return array


selection_sort2(input2)
print(input2)

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort2([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort2([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort2([100,56,-3,32,44]))