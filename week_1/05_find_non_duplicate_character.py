# 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫 번째 문자를 반환하기
# 그런 문자가 없다면 _를 반환하기
# 소문자만 문자열로 주어진다고 가정한다.


input = "abadabac"

# 소문자 26개의 빈도를 세는 리스트를 마련해서, 최종적으로 카운트가 1이 된 첫 문자를 반환한다:
# => 실패. 첫 번째 문자가 아니라 사전상 첫 번째 문자가 반환되게 된다.
def find_not_repeating_character1(string):
    alphabet_count_list = [0] * 26
    for char in string:
        alphabet_count_list[ord(char) - ord('a')] += 1
    for index in range(len(alphabet_count_list)):
        if alphabet_count_list[index] == 1:
            return chr(index + ord('a'))
    return "_"

# '버려진 알파벳'이 들어가는 리스트를 하나 더 마련해서, '카운트용 리스트'에서 하나씩 빼거나 넣을 때마다 버려진 리스트도 확인하게 하기:
def find_not_repeating_character2(string):
    unique_characters = []
    discarded_characters = []
    for char in string:
        if char not in unique_characters and char not in discarded_characters:
            unique_characters.append(char)
        elif char in unique_characters:
            unique_characters.remove(char)
            discarded_characters.append(char)
    return unique_characters[0] if len(unique_characters) != 0 else '_'

# ordered dict 이용하기(=넣은 순서가 보장되는)


result = find_not_repeating_character2("aabaecd")
print(result)