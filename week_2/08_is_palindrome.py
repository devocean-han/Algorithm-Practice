# Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.
# "abcba" # True

input = "abddba"


def is_palindrome(string):
    flipped_string = string[::-1]
    return string == flipped_string


# 강의판 정답1.
def is_palindrome2(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True


# 강의판 힌트를 얻어 재귀 함수 사용한 버전 (강의판과 오 완전 같음):
def is_palindrome3(string):
    # factorial(n) = n * factorial(n - 1) ... => factorial(1) = 1이 되었던 것처럼,
    # is_palindrome(문자) = 문자 체크 is_palindrome(다음 문자) ... => is_palindrome(가운데문자) = True..?
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return is_palindrome3(string[1:-1])


print(is_palindrome(input))
print(is_palindrome2(input))
print(is_palindrome3(input))