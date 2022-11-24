
# 최대힙에 원소 추가하기:
# 1. 완전 이진 트리인 힙의 가장 마지막 자리에 원소를 추가한다
# 2. 그 부모되는 노드와 값을 비교해서 (추가된)자식이 더 크면 부모와 자리를 바꾼다.
# 3. 부모보다 작거나 같아질 때까지, 혹은 루트 노드에 도달하게 될 때가지 위의 과정을 반복한다.

# 인덱스 기반으로 부모와 자식 찾는 규칙:
# 1. 현재 인덱스 * 2 -> 왼쪽 자식의 인덱스
# 2. 현재 인덱스 * 2 + 1 -> 오른쪽 자식의 인덱스
# 3. 현재 인덱스 // 2 -> 부모의 인덱스 (부모*2 와 부모*2+1 모두 한 부모를 가리킬 테니까)

class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 내 버전:
    # 시간 복잡도: 완전 이진트리의 최대 높이는 O(log(N))이므로
    # 반복하는(트리를 타고 올라가는) 최대 횟수도 O(log(N))이 된다.
    def insert1(self, value):
        # 1. 힙 끝에 추가
        self.items.append(value)

        # 1.1 추가된 자리가 루트 노드라면 그대로 정착함
        if len(self.items) <= 2:
            return self.items

        # 2. 부모와 비교 -> 자식(본인)이 더 크면 자리바꿈
        child_index = len(self.items) - 1
        parent_index = child_index // 2
        while child_index > 1 and self.items[child_index] > self.items[parent_index]:
            self.items[child_index], self.items[parent_index] = \
            self.items[parent_index], self.items[child_index]
            child_index = parent_index
            parent_index = child_index // 2

        return self.items

    # 강의판 해답:
    def insert2(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break


max_heap = MaxHeap()
max_heap.insert2(3)
max_heap.insert2(4)
max_heap.insert2(2)
max_heap.insert2(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!