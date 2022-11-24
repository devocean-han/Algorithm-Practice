
# # 병합 정렬: '합치면서 정렬이 되는' 개념이기 때문에 '분할 정복'으로 가능한 것!
# 병합 정렬은 배열의 앞부분과 뒷부분의 두 그룹으로 나누어 각각 정렬한 후
# 병합하는 작업을 반복하는 알고리즘입니다.
#
# [1, 2, 3, 5]  # 정렬된 배열 A
# [4, 6, 7, 8]  # 정렬된 배열 B
# [] # 두 집합을 합칠 빈 배열 C
#
#         ↓
# 1단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         1과 4를 비교합니다!
#         1 < 4 이므로 1을 C 에 넣습니다.
#      C:[1]
#
#            ↓
# 2단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         2와 4를 비교합니다!
#         2 < 4 이므로 2를 C 에 넣습니다.
#      C:[1, 2]
#
#               ↓
# 3단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         3과 4를 비교합니다!
#         3 < 4 이므로 3을 C 에 넣습니다.
#      C:[1, 2, 3]
#
#                  ↓
# 3단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         5와 4를 비교합니다!
#         5 > 4 이므로 4을 C 에 넣습니다.
#      C:[1, 2, 3, 4]
#
#                  ↓
# 3단계 : [1, 2, 3, 5]
#            ↓
#        [4, 6, 7, 8]
#         5와 6을 비교합니다!
#         5 < 6 이므로 5을 C 에 넣습니다.
#      C:[1, 2, 3, 4, 5]
#
# 엇, 이렇게 되면 A 의 모든 원소는 끝났습니다!
#
# 그러면 B에서 안 들어간 원소인
#        [6, 7, 8] 은 어떡할까요?
# 하나씩 C 에 추가해주면 됩니다.
#      C:[1, 2, 3, 4, 5, 6, 7, 8] 이렇게요!


## 일단 '병합'하는 파트:
array_a = [1, 3, 4, 5]
array_b = [2, 6, 7, 8]


# 나의 방법 1: 시간 복잡도는 정확히 array1과 array2의 길이를 더한 만큼. 즉, O(N)
def merge1(array1, array2):
    array_c = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            array_c.append(array1[i])
            i += 1
        else:
            array_c.append(array2[j])
            j += 1
    if i < len(array1):
        array_c += array1[i:]
    if j < len(array2):
        array_c += array2[j:]
    return array_c

# 내 방법 2: break로 구현하는 게 더 앗쌀할 것 같은데(?)
# => 중간에 어떻게 하는지 모르겠다...
def merge2(array1, array2):
    array_c = []
    for i in range(len(array1)):
        start_j = 0
        if start_j == len(array2)-1:
            array_c += array1[i:]
            break

        for j in range(start_j, len(array2)):
            if array1[i] <= array2[j]:
                array_c.append(array1[i])
                break
            else:
                array_c.append(array2[j])
            start_j = j
    array_c += array2[j:]
    return array_c


print(merge1(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
print(merge2(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다! => 망했다.


###########################################################
## 병합을 반복하며 정렬하기 파트:
# 분할 정복과 재귀 함수를 이용한다
# MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))

array = [5, 3, 2, 1, 6, 8, 3, 3, 7, 4, 11, 30, 23, 0]


# 시간 복잡도: 병합하는 각 단계에서 O(N)만큼의 시간 복잡도를 가진다.
# '각 단계'는 반으로 자르고 잘라서 요소 개수를 1로 만든 단계 => k단계에서 1개로 만들었다고 할 때,
# N / (2^k) = 1   =>  k = log_2(N)이다.
# 따라서 총 시간 복잡도는 O(N * logN)
def merge_sort(array):
    # 탈출 조건: mid로 나뉘어 나뉘어 요소를 1개만 가지게 되면. (다시 거슬러 올라가기)
    if len(array) <= 1: # 그냥 확실히 '1'이 되는 순간이 포착되는 거 아닌가? 왜 1보다 작아지는 경우를 생각해야 하지?
        return array
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])  # 여기까지는 분할이 되고,
    return merge1(left_array, right_array) # 여기서 병합이 이루어지게 된다.
                                           # 왼쪽의 왼쪽의 왼쪽의 ... 왼쪽 가지부터 순차적으로.

print(merge_sort(array)) # 잘 된다.