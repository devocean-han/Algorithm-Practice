# Q2. ✍️ 올바른 괄호
# Q.
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서
# ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어
#
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.
#
# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

# "(())()" # True
# "(((("   # False

# => 스택을 이용해서, 스택에는 열림 '('만 저장한다.
# => 만약 닫힘 ')'가 다음 문자열이면 스택에서 열림 '(' 하나를 뺀다.
# => 문자열이 다 닳았을 때 스택도 텅 비게 되면 통과.
# => ')'가 또 나왔는데 스택이 빈 상태거나, 문자열이 끝났는데 스택에 '('이 남아있는 상태라면 False.
# => 파이썬에서 스택은 리스트로!

# 내 해답: 
def is_correct_parenthesis1(string):
    stack = []
    for parenthesis in string:
        if parenthesis == '(':
            stack.append(parenthesis)
        else:
            if len(stack) == 0:
                return False  # 여는 괄호 '('가 부족했다.
            stack.pop()
    return len(stack) == 0  # 닫는 괄호 ')'가 부족했다면 False를 반환할 것임.


# 강의판 해답: (미안하지만 내 것이 훨씬 더 깔끔하다. 변수명마저도 그렇다. 흠흠)
def is_correct_parenthesis2(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)  # 여기 아무런 값이 들어가도 상관없습니다! ( 가 들어가있는지 여부만 저장해둔 거니까요
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis1("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis1(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis1("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis1("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis1("((())"))
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis1("((())())"))