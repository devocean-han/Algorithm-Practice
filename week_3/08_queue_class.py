# 큐(queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 꼬리에 추가
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    # 머리에서 빼내기
    def dequeue(self):
        if self.is_empty():
            return "Cannot dequeue. (the Queue is empty!)"
        dequeued_node = self.head
        self.head = self.head.next
        return dequeued_node.data

    # 머리에 뭐있나 정찰
    def peek(self):
        if self.is_empty():
            return "Cannot peek. (the Queue is empty!)"
        return self.head.data

    # 비었으면 True 반환
    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.peek())
