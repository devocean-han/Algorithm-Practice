# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
#
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# [6] -> [7] -> [8]
# [3] -> [5] -> [4]
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
#
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

# from week_1.01_print_linked_list import linkedList

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
            print(cur.data)
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
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

##
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

def _get_linked_list_sum(linked_list):
    node = linked_list.head
    sum = 0
    while node is not None:
        sum = (sum * 10) + node.data
        node = node.next
    return sum

def get_linked_lists_sum(linked_list_1, linked_list_2):
    return _get_linked_list_sum(linked_list_1) + _get_linked_list_sum(linked_list_2)

print(get_linked_lists_sum(linked_list_1, linked_list_2))