# 정수를 받아, 그 정수 이하의 소수를 모두 반환하기
from math import floor

input = 20


def find_prime_list_under_number1(number):
    prime_list = []
    for num in range(2, number+1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


# 주어진 수가 소수이면 True 반환
def is_prime(number):
    # print(number, " : ", int(number**0.5), " => 2 ~ ", int(number**0.5)+1)
    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            return False
    return True

result = find_prime_list_under_number1(input)
print(result)


# 정답 버전1 - 나누는 수를 2부터 모든 수로 잡아 검사하기:
def find_prime_list_under_number2(number):
    prime_list = []
    for num in range(2, number + 1):
        for i in range(2, num): # 1과 '자기자신'을 제외하고 (나누어 떨어지는지)검사
            if num % i == 0:
                break # 바로 다음 '소수 후보'로 넘어가서 검사 다시 시작
        else: # 한 '소수 후보'에 대해 검사를 '자기자신'-1까지 오도록 하였는데 나누어 떨어지지 않았으므로 이것은 소수!
            prime_list.append(num)
    return prime_list

# 정답 버전2 - 나누는 수를 소수로만 한정지어서 검사하기:
# 여기서부터 이해가 잘 안된다. 왜 소수로만 나누기를 검사한다는 거지..?
def find_prime_list_under_number3(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

# 정답 버전3 - 나누는 수를 소수로 한정짓고, 본체 수의 제곱근까지만 검사하기:
# 제곱근까지만 검사하는 건 알고 있는 트릭이다. 근데 코드가 이해가 잘;;
# if 조건에 i * i >= n이면 break하라고 해야 하는거 아냐??
# 그리고 어차피 for문에서 한 번씩 다 들어와서 검사하고 가는데 뭐가 효율적이라는 거지?
def find_prime_list_under_number4(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list

print(find_prime_list_under_number4(30))