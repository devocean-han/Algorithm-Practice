# Q. 피보나치 수열의 20번째 수를 구하시오.

# 피보나치 수열 1, 1, 2, 3, 5, 8, 13, 21, ...을 재귀 함수로 구현하기
# F(N) = F(N-1) + F(N-2)의 반복되는 형태임.

input = 20


def fibo_recursion(n):
    if n <= 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765