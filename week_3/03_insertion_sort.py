# 삽입 정렬: 차례로 검사해서 자신의 올바른 위치를 찾아들어가는 방식.

# 이번에는 선택 정렬과는 조금 느낌이 다릅니다!
#
# 선택 정렬이 전체에서 최솟값을 "선택" 하는 거 였다면,
# 삽입 정렬은 전체에서 하나씩 올바른 위치에 "삽입" 하는 방식입니다!
#
# 선택 정렬은 현재 데이터의 상태와 상관없이 항상 비교하고 위치를 바꾸지만,
# 삽입 정렬은 필요할 때만 위치를 변경하므로 더 효율적인 방식입니다!


input = [4, 6, 2, 9, 1]


# 내 버전:
def insertion_sort(array):
    for i in range(1, len(array)): # 자리를 찾아들어가야 하는 신병이 되는 i
        while array[i - 1] > array[i] and i >= 1: # 비교가 필요한 (이미 정렬된) 선임 j들
            array[i - 1], array[i] = array[i], array[i - 1]
            i = i - 1
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


# 강의판 버전: O(N^2) 이지만 운이 좋으면(=최선의 경우) O(N)으로 끝낼 수 있다.
def insertion_sort2(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

input2 = [4,7,2,3,6,9,1,8,5,0]
insertion_sort2(input2)
print(input2)

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort2([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort2([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort2([100,56,-3,32,44]))