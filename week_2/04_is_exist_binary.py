# target이 array에 존재하면 True를 반환

finding_target = 16
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2
        ## 0, 7, 15
        ## 8, 11, 15
        ## 12, 13, 15 # 찾는 수가 14면 여기서 발견!
        ## 14, 14, 15 # 찾는 수가 15면 여기서 발견!
        ## 15, 15, 15 # 찾는 수가 16(가장 끝)이면 여기서 발견!
        ## 만약 찾는 수가 20이었다면 이제는 16, ?, 15가 되어 while 루프를 벗어나게 됨. 그리고 False 반환.
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)