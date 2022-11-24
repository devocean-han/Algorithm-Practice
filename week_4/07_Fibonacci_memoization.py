# Q. 피보나치 수열의 100번째 수를 구하시오.
#
# 재귀함수로 피보나치 수열을 구현했을 때,
# 계속 똑같은 문제를 다시 푸는 바람에 목표를 달성하지 못했습니다!
#
# 이번에는, 새로 배운 동적 계획법의 메모이제이션이라는 방법을 통해서 해결해보도록 하겠습니다!
#
# 구현의 방법은 다음과 같습니다.
# 1. 메모용 데이터를 만든다. 처음 값인 Fibo(1), Fibo(2) 는 각각 1씩 넣어서 저장해둔다.
# 2. Fibo(n) 을 구할 때 만약 메모에 그 값이 있다면 바로 반환한다.
# 3. Fibo(n) 을 처음 구했다면 메모에 그 값을 기록한다.


input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo1 = {
    1: 1,
    2: 1
}
memo2 = {
    1: 1,
    2: 1
}


# 내 해답:
def fibo_dynamic_programming1(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    # n <= 2인 경우를 따로 적어줄 필요가 없다. memo에 들어가서 이미 확인했을 것이기 때문에.
    fibo_n = fibo_dynamic_programming1(n - 1, fibo_memo) + fibo_dynamic_programming2(n - 2, fibo_memo)
    fibo_memo[n] = fibo_n
    return fibo_n


# 강의판 해답: 완전히 똑같음!
def fibo_dynamic_programming2(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming2(n - 1, fibo_memo) + fibo_dynamic_programming2(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming1(input, memo1))
print(fibo_dynamic_programming2(input, memo2))