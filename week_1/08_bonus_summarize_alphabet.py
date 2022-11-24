# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
#
# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.

# Ex 1)
# abc 	# a1/b1/c1
#
# Ex 2-1)
# aaabbbc	# a3/b3/c1
#
# Ex 2-2)
# abbbc	# a1/b3/c1
#
# Ex 3-1)
# ahhhhz	# a1/h4/z1
#
# Ex 3-2)
# acccdeee	# a1/c3/d1/e3

# 내 코드
def summarize_string1(input_str):
    current_alphabet = input_str[0]
    count = 1
    result = []
    for char in input_str[1:]:
        if char == current_alphabet:
            count += 1
        else:
            result.append(current_alphabet + str(count))
            current_alphabet = char
            count = 1
    result.append(current_alphabet + str(count))
    return '/'.join(result)

# 정답 코드 - '지금'인덱스를 '다음' 인덱스와 비교, 문자열로 바로 넣고 '/'도 덧붙임
def summarize_string2(input_str):
    count = 0
    result_str = ''
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            result_str += input_str[i] + str(count + 1) + '/'
            count = 0

    result_str += input_str[len(input_str) - 1] + str(count + 1)
    return result_str

print(summarize_string1("annnddw"))
print(summarize_string2("annnddw"))