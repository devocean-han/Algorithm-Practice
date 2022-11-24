# 알파벳 최빈값 찾기
input = "hello my name is sparta"


# A = 65
# a = 97
# ord('a') = 97


def find_max_occurred_alphabet(string):
    alphabet_list = [0] * 26
    for char in string.replace(' ', ''):
        alphabet_list[ord(char) - ord('a')] += 1
    print(alphabet_list)
    return chr(alphabet_list.index(max(alphabet_list)) + ord('a'))


# 알파벳 하나씩 정해서 문자열 전체를 돌면서, 이전 최빈값보다 더 크면 이전 것을 덮어씌우는 방식:
def find_max_occurred_alphabet2(string):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    max_occurrence = 0
    max_occurred_alphabet = alphabets[0]
    for alphabet in alphabets:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        if max_occurrence < occurrence:
            max_occurrence = occurrence
            max_occurred_alphabet = alphabet
    return max_occurred_alphabet


result = find_max_occurred_alphabet(input)
print(result)
print(find_max_occurred_alphabet2('hamilton lover'))
