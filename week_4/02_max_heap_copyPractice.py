class MaxHeap2:
    def __init__(self):
        self.items = [None]

    # 새 숫자 넣기.
    def add(self, data):
        # 1. 가장 마지막 자리에 원소 추가
        self.items.append(data)

        # 2. 부모와 값 비교후 자리바꿈 반복
        child_index = len(self.items) - 1

        while child_index > 1:
            parent_index = child_index // 2
            if self.items[child_index] > self.items[parent_index]:
                self.items[child_index], self.items[parent_index] = self.items[parent_index], self.items[child_index]
                child_index = parent_index
            else:
                break

    # 원소 뽑기
    def pop(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        popped = self.items[-1]
        self.items = self.items[:-1]

        parent_index = 1
        while (parent_index * 2) + 1 <= len(self.items):
        # 부모에게 왼 자식이 있다는 것만 보장했더니, 오른 자식을 검사하는 부분에서 에러가 났다.
        # 정말 정확하군. 그래서 오른 자식이 있다는 것까지 보증했다 => parent * 2 + 1
        # => 하지만 작동하지 않았다. 저 조건 어디에 문제가 있는 건지 잘 모르겠군. 너무 졸리다.
            max_index = parent_index
            left_child_index = parent_index * 2
            right_child_index = (parent_index * 2) + 1
            # max_index = max(self.items[parent_index], self.items[left_child_index], self.items[right_child_index])

            # 왼 자식이 지금의 max_index(=부모)보다 크면 우선 왼 자식을 max_index로 추대:
            if self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            # 그 다음 또 오른쪽 자식이 지금의 max_index보다 크면 오른 자식을 max_index로 추대:
            if self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            # 위의 두 과정을 거쳐, 이제는 부모, 왼 자식, 오른 자식 셋 중 하나가 적절하게 max_index일 것이므로:
            # 아, 그전에 만약 부모가 여전히 max_index인 채로라면 바꿀 것도 없고, 그대로 종료.
            if max_index == parent_index:
                break

            self.items[max_index], self.items[parent_index] = self.items[parent_index], self.items[max_index]
            parent_index = max_index

        return popped


max_heap2 = MaxHeap2()
max_heap2.add(5)
max_heap2.add(6)
max_heap2.add(7)
max_heap2.add(5)
max_heap2.add(10)
max_heap2.add(8)
max_heap2.add(9)
print(max_heap2.items)

# for i in range(len(max_heap2.items) - 1):
#     print(max_heap2.pop())
print(max_heap2.pop())
# while len(max_heap2.items) > 1:
#     print(max_heap2.pop())