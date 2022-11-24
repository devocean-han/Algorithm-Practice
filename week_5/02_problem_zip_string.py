# ✍️ 문자열 압축
#
# Q. 데이터 처리 전문가가 되고 싶은 어피치는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
#
# 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여
# 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
#
# 간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)
# 와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이
# 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한
# 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수
# 있는지 방법을 찾아보려고 합니다.
#
# 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,
# 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다. 다른 방법으로 8개
# 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할
# 수 있는 방법입니다.
#
# 다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가
# 되지만, 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.
# 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
#
# 압축할 문자열 input이 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로
# 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록
# string_compression 함수를 완성해주세요.
#
# * 문자열의 길이는 1 이상 1,000 이하입니다.
# * 문자열은 알파벳 소문자로만 이루어져 있습니다.
#
# 이 때, 문자열은 항상 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 입출력 예 #5 처럼 xababcdcdababcdcd 이 입력되어도,
# 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능합니다.
# 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.
#
# "aabbaccc"	# -> 2단위: 2a2ba3c / 7
# "ababcdcdababcdcd"	# -> 2단위: 2ab2cd2ab2cd / 12 , 4단위: 2ababcdcd / 9
# "abcabcdede"	# -> 2단위: abcabc2de / 9, 3단위: 2abcdede / 8
# "abcabcabcabcdededededede"	# -> 6단위: 2abcabc2dedede / 14
# "xababcdcdababcdcd"	# -> 17

# => 1부터 문자열 길이만큼까지의 단위로 잘라가면서 하나하나 결과값을 비교해보자...



input = "abcabcabcabcdededededede"


def string_compression1(string):
    print(f'주어진 문자열 : {string}')
    zip_results = []
    for unit in range(1, len(string) + 1): # 잘라볼 단위, unit
        result = ''
        repeat_count = 1

        # 예를 들어 unit=3일 때, 3문자씩 잘라서 압축(비교)해봄:
        print(f'\n{unit} 로 잘라보는 시간...')
        for i in range(0, len(string) - unit, unit):
            print(f'지금 뭉치 vs. 다음 뭉치 : {string[i:i + unit]} vs {string[i + unit: i + (2*unit)]}')
            if string[i:i + unit] == string[i + unit: i + (2*unit)]:
                repeat_count += 1
            else:
                # 단위 문자가 반복된 횟수가 1 초과면 반복 횟수도 같이 기록해줌.
                if repeat_count > 1:
                    result += str(repeat_count)
                result += string[i:i + unit]
                repeat_count = 1
        if repeat_count > 1:
            result += str(repeat_count)
        # result += string[-unit:] # 남은 게 정확히 unit 개 만큼이 아닐 수도 있다. 흠...
                # 그냥 남은 거 전부 붙이면 될 것 같은데. 분명 unit보다 적거나 같은 개수가 남아있을 것이다.
                # 남은거... for 루프 안에서 마지막 인덱스를 기억해야 할 것 같은데.
                # for문 안의 인덱스를 어떻게 기억해서 나오지? 그냥 쌩으로 계산해야 하나...
                # 일단 unit이 있으니까, len(string) % unit값이 0이면 unit만큼 마지막에 붙이고,
                # 0아니고 다른 값이면 그 수만큼 마지막에 붙이고!
        remaining_index = len(string) % unit
        if remaining_index == 0:
            result += string[-unit:]
        else:
            result += string[-remaining_index:]

        zip_results.append(result)

    print(zip_results)
    return min(len(result) for result in zip_results)


# 강의판 해답:
# 오오오 사실 1부터 n//2까지만 잘라보면 된다!
# 그리고 저 splited 리스트 주목. 한 번에 자르고 이중 리스트까지 만들어 버리기.
def string_compression2(string):
    n = len(string)
    compression_length_array = []  # 1~len까지 압축했을때 길이 값

    for split_size in range(1, n // 2 + 1):
        compressed = ""
        # string 갯수 단위로 쪼개기 *
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:  # 이전 문자와 다르다면
                if count > 1:
                    compressed += (str(count) + prev)
                else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
                    compressed += prev
                count = 1  # 초기화
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
            compressed += splited[-1]
        compression_length_array.append(len(compressed))

    return min(compression_length_array)  # 최솟값 리턴


print(string_compression2(input))  # 14 가 출력되어야 합니다! => 됐다!!


print("정답 = 3 / 현재 풀이 값 = ", string_compression2("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression2("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression2('BBAABAAADABBBD'))