# # BOJ 1874번 <스택 수열>
#
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이
# 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로
# push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
#
# 입력 예시:
# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1
# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다.
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
# 물론 같은 정수가 두 번 나오는 일은 없다.
#
# 출력 예시:
# +
# +
# +
# +
# -
# -
# +
# +
# -
# +
# +
# -
# -
# -
# -
# -
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
# push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
#
#
# 입력 예시 2:
# 5
# 1
# 2
# 5
# 3
# 4
#
# 출력 예시 2:
# NO


# => 1. 우선 같은 수가 2번 입력되면 안 된다.
# => 2. 첫 입력으로 만나는 수(4)에 도달할 때까지 push하고(1->2->3->4), 뽑는다(pop=4)
# => 3. 그 다음 입력으로 만나는 수는 '지금스택'.peek()이든가, 아니면 금방 뽑혀나간 애(4)보다 커야 한다.
def stack_sequence1(n, sequence):
    stack = []
    result_push_pop = []
    next_to_push = 1
    for num in sequence:
        if num < next_to_push:
            if stack[-1] != num:
                return "NO"
            else:
                stack.pop()
                result_push_pop.append('-')
        else:
            while next_to_push <= num:
                stack.append(next_to_push)
                result_push_pop.append('+')
                next_to_push += 1
            stack.pop()
            result_push_pop.append('-')
    return result_push_pop


sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
print(stack_sequence1(n, sequence))


# 강의판 해답: (해석은 나중에...)
def stack_sequence2(n, sequence):

    stack = []
    num = 1
    sequence_idx = 0
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1

        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_idx += 1
            if sequence_idx == n:
                break

        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for char in result:
            print(char)


sequence = list()

n = int(input())
for _ in range(n):
    sequence.append(int(input()))

stack_sequence2(n, sequence)