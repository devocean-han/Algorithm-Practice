class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
print(node.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.length = 1

    # 끝에 원소 추가
    def append(self, data):
        # head 자체가 None인 경우, head에 data를 넣어주기:
        if self.head is None:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next is not None:
            print("cur is ", cur.data)
            cur = cur.next
        cur.next = Node(data)
        self.length += 1

    # 원소 전체 출력
    def print_all(self):
        # cur = self.head
        # temp_list = [cur.data]
        # for i in range(self.length):
        #     cur = cur.next
        #     temp_list.append(cur.data)
        # return temp_list
        print()
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        # 왜 꼭 마지막에 None이 출력되는 건지 모르겠다...
        # => print_all()을 print()안에 불렀기 때문이다.
        # => return 값이 없는 걸 print()안에 부르면 리턴값이 None으로 출력되므로.

    # index번째 원소 반환
    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
            if cur.next is None:
                print(f"현재 링크드리스트의 길이가 주어진 인덱스보다 작으므로 마지막 노드(인덱스 {i+1})를 반환합니다.")
                break
        return cur

    # index번째에 원소 추가
    def append_at(self, index, data):
        new_node = Node(data)

        # get_node()는 0까지밖에 노드를 찾아줄 수 없으므로.
        # 내가 필요한 건 0 - 1번째의 노드가 될 텐데.
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            temp_node = cur.next
            cur.next = Node(data)
            cur.next.next = temp_node

    # 강의판: 근데 이렇게 하면 index 다음 칸에 넣게 되는 거 아님?
    def append_at2(self, index, data):
        node = self.get_node(index)
        temp_node = node.next
        node.next = Node(data)
        node.next.next = temp_node
    # ㅇㅇ. 그래서 index번째 노드를 잡아오는 게 아니고 index-1번째 노드를 잡아오고,
    # 그러면 index=0이 들어온 경우를 예외처리해 주면 내가 위에서 작성한 것과 같은 코드가 됨:
    def append_at3(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_target_node = self.get_node(index - 1)
            new_node.next = prev_target_node.next
            prev_target_node.next = new_node

    # index번째 원소 삭제
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list.print_all())

print()
linked_list.append_at(1, 0)
# print(linked_list.get_node(0).data)
linked_list.append_at(0, 10)
print(linked_list.print_all())
linked_list.append_at3(0, 20)
print(linked_list.print_all())
linked_list.delete(5)
print(linked_list.print_all())
linked_list.print_all()