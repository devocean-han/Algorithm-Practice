# 링크드 리스트의 끝에서 k번째 노드 반환하기
# 5 -> 6 -> 7 -> 8 이고 k = 2라면, 7 노드를 반환하도록.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last1(self, k):
        # 먼저 전체 한 바퀴를 돌면서 길이를 알아내서
        length = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            length += 1
        cur = self.head

        # 전체 길이 - k 번째의 노드를 얻으면 된다.
        for i in range(length - k):
            cur = cur.next
        return cur

    # 포인터 두 개를 두고 찾는 방법!
    # 찾아야 하는 위치보다 k만큼 앞서간 포인터를 두고, 앞선 포인터가 끝을 만나면 뒤따르는 포인터를 반환!
    def get_kth_node_from_last2(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None: # 이 while을 탈출하게 되는 때는 fast가 범위 밖까지(끝보다 한 칸 더) 나가고 난 후!
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)


print(linked_list.get_kth_node_from_last1(2).data)  # 9가 나와야 합니다!
print(linked_list.get_kth_node_from_last2(4).data)  # 7이 나와야 합니다!