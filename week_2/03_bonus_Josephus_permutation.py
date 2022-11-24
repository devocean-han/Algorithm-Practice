
# BOJ 1158

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을
# 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어
# (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
#
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# => (7, 3)이면 7명이 원을 그리고 앉아있는데 3번째 사람들을 제거해 나간다. ...아~
# => 처음은 무조건 3(K)번째 사람일 거고, 그 다음 6번째, 그다음 2, 5, 1, 4, 앗 아니다. 빠진 사람들은 건너 뛰어야 한다.
# => 누구누구를 건너 뛰어야 하는지 어떻게 기록하지..? 그냥 1부터 N까지 리스트에 집어넣어 놓고 3의 배수 인덱스마다 빼버려?

# => 알았다. linkedList 노드를 삭제하는 방식으로 가면 된다. 마지막 노드는 다시 head를 가리키게 하고.
# => 연결에서 끊어진 노드(=삭제당한 노드)도 여전히 '다음으로의 연결'은 남아 있어서 .next.next.next로
# => 본류의 다음 3번째 애를 찾아가는 게 가능해서 가능한 방법!!

## 강의판 Node 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## 강의판 LinkedList 클래스
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end='')
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node
        node = self.get_node(index - 1)
        deleted_node = node.next
        node.next = node.next.next
        return deleted_node

def josephus_problem(n, k):
    # 노드가 1부터 n까지 n개.
    # .next를 해야 하는 개수가 k번씩.
    # 처음에 k번째 노드를 곧바로 찾아가서 삭제 후
    # 삭제한 노드로부터 k번 .next를 떼려 도착한 노드를 순차적으로 삭제해 나가면 된다.
    # 그리고 삭제당한 노드의 data를 순서대로 list 등에 넣어서 반환하면 되겠다.

    # 1. linkedList 만들기
    linked_list = LinkedList(1)
    for i in range(2, n + 1):
        linked_list.append(i)

    # 2. 반환할 요세푸스 순열을 담을 리스트
    result_list = []

    # 3. 처음에 k번째 노드를 곧바로 찾아가 삭제 후 그 값 리스트에 넣기
    deleted_node = linked_list.delete_node(k - 1)
    result_list.append(deleted_node.data)
    print(linked_list.print_all())

    # 4. 삭제한 노드로부터 k번째를 삭제 후 그 값 리스트에 넣기를 반복
    #    head 노드 하나만 남을 때까지 (노드가 하나 뿐이면 앞으로(.next) 갈 수가 없으므로)
    while linked_list.head.next is not None:
        for i in range(k - 1):
            # linked_list.get_node(n - 1).next = linked_list.head # 꼬리가 head를 가리키게 만들기
            # 꼬리에 다다랐으면 head로 다시 향하게 하기
            if deleted_node.next is None:
                deleted_node = linked_list.head
            else:
                deleted_node = deleted_node.next
        node = deleted_node
        deleted_node = node.next
        node.next = node.next.next
        result_list.append(deleted_node.data)
        print(linked_list.print_all())
        print(result_list)

    # 5. head 노드도 요세푸스 순열에 담기
    result_list.append(linked_list.head.data)

    # 6. <3, 6, 2, 7, 5, 1, 4>과 같은 모양으로 출력하기
    print(result_list)
    return result_list



# n, k = map(int, input().split())
# print(josephus_problem(7, 3))


## 헐 강의판 정답 해설:
# BOJ 1158

def josephus_problem2(n, k):
    result_arr = []

    next_index = k - 1
    people_arr = list(range(1, n + 1))

    while people_arr:
        result = people_arr.pop(next_index)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_index = (next_index + (k - 1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split())
josephus_problem2(n, k)