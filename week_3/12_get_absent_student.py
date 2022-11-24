
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# 내 방법: set 두번 => N + (N-1), 그리고 N-1번만큼 검사후 빼기.
# 따라서 시간 복잡도는 O(3N) => O(N)이다.
def get_absent_student1(all_array, present_array):
    return (set(all_array) - set(present_array)).pop()


print(get_absent_student1(all_students, present_students))


# 강의판 해법: 딕셔너리 키에 넣었다 빼기(키는 O(1)시간만에 찾아 들어갈 수 있는 해쉬 자료구조니까!)
# 시간 복잡도는 N + (N-1) => O(2N) => O(N)이다.
# 공간 복잡도도 O(N)이다. 모든 학생을 다 해쉬 테이블 내에 저장하므로.
# => 해쉬 테이블은 시간은 빠르되 공간을 대신 사용하는 자료구조임.
def get_absent_student2(all_array, present_array):
    dict = {}
    for key in all_array:
        dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요

    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
        return key


print(get_absent_student2(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student1(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student1(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))