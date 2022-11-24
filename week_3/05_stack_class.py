# 스택(stack): 나중에 들어간 게 먼저 나오는 자료구조.
# '되돌리기(ctrl + z)', '이전 페이지로 돌아가기' 등의 기능을 구현하는 데 유용하다.
# '자주 넣고 빼야 하는' 자료구조이므로 링크드 리스트가 적합함
# (근데 맨 끝에 넣고 빼는 건 어레이 리스트도 좋다고 하지 않음?)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self.head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "the Stack is empty!"
        popped_node = self.head
        self.head = self.head.next
        return popped_node

    def peek(self):
        return self.head

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek().data)
print(s.pop().data)
print(s.peek().data)
print(s.pop().data)
print(s.is_empty())
print(s.pop().data)
print(s.is_empty())
print(s.pop()) # 잘 된다.