# ✍️ 올바른 괄호 문자열 만들기
#
# Q.
# 카카오에 신입 개발자로 입사한 콘은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한
# 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다. 소스를 컴파일하여
# 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어
# 오류가 나는 것을 알게 되었습니다.
# 수정해야 할 소스 파일이 너무 많아서 고민하던 콘은 소스 코드에 작성된 모든 괄호를 뽑아서
# 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.
#
# 용어의 정의 :
# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면
# 이를 균형잡힌 괄호 문자열이라고 부릅니다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
# 예를 들어, "(()))("와 같은 문자열은 균형잡힌 괄호 문자열 이지만 올바른 괄호 문자열은 아닙니다.
# 반면에 "(())()"와 같은 문자열은 균형잡힌 괄호 문자열 이면서 동시에 올바른 괄호 문자열 입니다.
#
# '(' 와 ')' 로만 이루어진 문자열 w가 균형잡힌 괄호 문자열 이라면 다음과 같은 과정을 통해
# 올바른 괄호 문자열로 변환할 수 있습니다.
#
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로
# 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.
#
# 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로
# 변환한 결과를 반환하시오.
#
# "(()())()"	# -> "(()())()"
# ")("        # -> "()"
# "()))((()"	# -> "()(())()"

# => 괄호 개수는 맞춰서 입력이 주어짐. 열리고 닫힘까지 맞도록 바꿔서 반환하기.
# => 빈 문자열이면 빈 문자열 반환
# => (()())()같은 경우를 u, v로 나눈다면... (()())와 ()로 나눌 수 있겠지.
# => 앞 쪽의 v는 결국 열림과 닫힘 개수만 맞도록 자른 최소한의 단위이겠다.
# => 즉, 앞에서부터 열림 닫힘을 더하고 빼나가다 0이 되는 순간 u로 자르기.
# => 다음으로 남은 문자열에 대해 또 0이 되는 순간 u로 자르기 반복.
# => 근데 두 번째 u를 만들기 전에 u를 먼저 올바르게 되도록 처리한다.
# => '올바른지 아닌지'를 어떻게 알지?


balanced_parentheses_string = "()))((()"


# '올바른' 괄호 문자열이면 True 반환:
def is_correct_parenthesis(string):
    stack = []
    for parenthesis in string:
        if parenthesis == '(':
            stack.append(parenthesis)
        else:
            # ')'가 나왔는데 이미 남은 '('가 하나도 없는 상태인 경우, 틀렸음
            if len(stack) == 0:
                return False;
            stack.pop()
    # 끝까지 진행했는데 '('가 아직 남아있어도 틀렸음
    return len(stack) == 0


# '균형잡힌' 괄호 문자열이면 True 반환:
def is_balanced_parenthesis(string):
    return string.count('(') == string.count(')')


    # # 이게 뭔 소리지..?ㅍ=> 아하...
    # 예를 들어 (()())()의 경우, 1단계에서 u=(()()), v=()일 것이고,
    # 그러면 u는 올바른 괄호문자열이므로 v에 대해 다시 자르기를 반복한다. u는 그대로 냅두고.
    # 2단계에서 u=(), v=''가 되고, 다시 u를 타겟팅했을 때 또 올바른 괄호문자열이므로 그대로 냅두고
    # v자르기로 넘어간다. 3단계에서 u='', v=''가 되고 u를 보니 빈 문자열이라 그대로 빈 문자열 반환,
    # 그럼 다시 2단계 레벨에서의 u=()에 돌려받은 결과 ''를 붙여서 반환하고,
    # 1단계 레벨에서 u=(()())에 돌려받은 '()'를 붙여서 반환하면
    # 최종적으로 (()())()가 반환된다.
    #
    # 예를 들어 )(같은 경우는,
    # 1단계 : u=)(, v='' 이 때 u가 올바르지 않으므로 4번 과정을 수행한다.
    #     '(' + v에 대해 재귀반복 결과(='') + ')' +
    #     여기에 u의 첫 번째와 마지막을 제거하면 '', 나머지 문자열의 괄호 방향을 뒤집어도 ''
    #     최종 반환되는 문자열은 따라서 '()'
    # 이게 끝인가? 그냥 최종 반환이야?
    #
    # 예르 ㄹ들어 ()))((() 같은 경우,
    # 1단계 : u=(), v=))(((). u는 올바르므로 그대로 남아있고,
    # 2단계 : u=))((, v=(). u가 올바르지 않으므로 4번 괒어을 수행한다.
    #     '(' + v에 대해 재귀반복한 결과 + ')' + u양끝 제거후 플립
    #     = '(' + v 결과값 + ')()' 반환하게 됨.   => 이게 1레벨로 돌아가서 1레벨의 u와 연결되게 된다.
    #     3단계 : 2단계 v에 대해 재귀반복 => u=(), v=''. u가 올바르므로 그대로 남아있고,
    #     4단계 : u='', v=''. 따라서 u의 ''가 그대로 반환되고,
    #     3단계로 돌아가서 u=()에 붙은 '()'가 반환되고,
    # 2단계로 돌아와 2단계가 반환하는 것은 결국 '(())()'이 되고,
    # 1단계에서 마지막으로 u=()과 결합해 최종적으로 '()(())()'이 반환되게 된다...


# 예시를 한 번 이해해보고 다시 풀어본 버전:
# 내가 이해하기로는 반환 지점이 3군데다.


# 전체 문자열을 u와 v로 쪼개고 쪼개는 데 필요한 쪼개기 함수.
# '균형잡힌' 문자열을 가장 작은 (첫) 균형잡힌 문자열 u와 나머지 문자열 v로 나눠 반환한다.
def get_separated_balanced_parenthesis(string):
    for i in range(1, len(string) + 1): # i=0부터 갈 경우 첫 판에 u = [:0] = ''이 되어 '균형잡혔다'고 통과되어버린다. => 무한루프행
        # 매번 i=1부터 검사하게 하면 '()'같이 2개 이하의 문자열이 들어왔을 때 i=1~1, 즉 '()'[:1]만 검사하고 끝내게 된다.
        # 그러면 결국 '()'[0]과 같으므로 마지막 2개 이하 문자는 절대로 is_balanced_p..()를 통과할 수 없다.
        # i를 1부터 문자길이+2까지 검사하게 해야 한다. 그래야 range에서 하나 잘리고 슬라이스에서 하나 잘려서 끝까지 검사할 수 있다.
        # => range(1, len(받은문자열) + 2)) : '()'가 들어오면 i=1,2,3을 돌게 되고, 슬라이싱에 들어가
        #   '()'[:1]과 '()'[:2], '()'[:3], 즉 '('과 '()'를 검사하게 된다. 엥? i=3은 없어도 되네.
        # 최종: range(1, len(받은문자열) + 1)
        if is_balanced_parenthesis(string[:i]):
            u = string[:i]
            v = string[i:]
            return u, v
            # 주어지는 문자열은 모두 '균형잡힌' 문자열이므로 끝에 갈 때 까지 반드시 한 번은
            # '균형잡힌' 문자열이 나와 u에 담기고 탈출하게 된다. 따라서 else: 신경 쓸 것 없음.


# 반환 지점 3(=u가 '올바르지 않은' 경우)에서 u의 괄호 방향을 뒤집어 주는 부분.
# 괄호 문자열을 받아서 괄호 방향을 뒤집은 새 문자열을 반환한다.
def flip_parenthesis(string):
    result = ''
    for parenthesis in string:
        if parenthesis == '(':
            result += ')'
        else:
            result += '('
    return result


# 재귀를 실행하는 전체 함수:
# 받은 문자열을 '가장 작은 균형잡힌 문자열' u와 그 나머지 v로 쪼개기를 반복하며
# u가 빈 문자열인 경우, u가 '올바른' 문자열인 경우, u가 올바르지 않은 문자열인 경우를 각각 나눠
# 탈출 1번, 재귀 분기 2번을 써서 '올바르게 만든' 문자열을 반환한다.
def get_correct_parentheses2(balanced_parenthesis_string):
    # (내가 추가:) 만약 주어진 문자열이 '균형잡힌' 문자열이 아니라면, '균형잡히지 않음' 표시로 None 반환
    if not is_balanced_parenthesis(balanced_parenthesis_string):
        return None
    # 오 만약 주어진 문자열이 '올바른' 문자열이라면, 곧바로 반환
    if is_correct_parenthesis(balanced_parenthesis_string):
        return balanced_parenthesis_string

    # 반환 지점 1: 탈출 조건. u=''가 된 경우.
    if len(balanced_parenthesis_string) == 0:
        return ''

    u, v = get_separated_balanced_parenthesis(balanced_parenthesis_string)

    # 반환 지점 2: u가 (빈 문자열이 아니고) 이미 올바른 경우
    if is_correct_parenthesis(u):
        return u + get_correct_parentheses2(v)

    # 반환 지점 3: u가 (빈 문자열이 아니고) 올바르지 않은 경우
    # else를 해주지 않아도 같은 결과가 될까..? => 같다.
    # else:
    return '(' + get_correct_parentheses2(v) + ')' + flip_parenthesis(u[1:-1])


# 강의판 해답:
# => is_correct_parenthesis()와 마지막 테스트 케이스 예시가 이상하다.
from collections import deque


def is_correct_parentheses(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            # '올바른' 괄호 문자열인가를 확인하는 것이므로 '균형잡힌' 괄호들이 들어오더라도
            # ')'의 차례에 충분히 스택이 비었을 수 있다. 여기를 처리해줘야 하는데 안 해줬다.
            stack.pop()
    return len(stack) == 0


# 이 부분도 큐를 굳이..?
def separate_to_u_v(string):  # u, v로 분리
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:  # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break

    v = ''.join(list(queue))
    return u, v


def reverse_parentheses(string):  # 뒤집기
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


def change_to_correct_parentheses(string):
    if string == '':  # 1번
        return ''
    u, v = separate_to_u_v(string)  # 2번
    if is_correct_parentheses(u):  # 3번
        return u + change_to_correct_parentheses(v)
    else:  # 4번
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


print(get_correct_parentheses2(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!


print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses2(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses2("))()("))
    # => 분명 '균형잡힌'애만 들어온다고 명시되어 있고 문제풀이도 그렇게 하는데 이런 테스트 케이스를 지정해놓는 이유는 무엇이란 말인가...
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses2(')()()()(())('))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses2(')()()()(())('))
print("정답 = (()())() / 현재 풀이 값 = ", get_correct_parentheses2('(()())()'))




