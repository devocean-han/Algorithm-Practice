
# 최대힙에서 원소 뽑기: 항상 루트 노드를 뽑아간다.
# 1. 루트와 끝 자리를 자리 교체한다.
# 2. 끝 자리에 오게 된 원래의 루트 노드를 변수에 따로 저장한 후 제거해준다.
# 3. 루트에 자리하게 된 원래의 맨 끝 노드를 자식 둘 중 더 큰 쪽과 비교해서,
# 4. 자신보다 크면 자리를 바꾼다.
# 5. 자기 자신이 리프 노드가 되거나(끝 레벨에 도달), 자식이 전부 자신보다 더 작거나 같다면 비교를 멈춘다.

# 인덱스 기반으로 부모와 자식 찾는 규칙:
# 1. 현재 인덱스 * 2 -> 왼쪽 자식의 인덱스
# 2. 현재 인덱스 * 2 + 1 -> 오른쪽 자식의 인덱스
# 3. 현재 인덱스 // 2 -> 부모의 인덱스 (부모*2 와 부모*2+1 모두 한 부모를 가리킬 테니까)

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 내 해답:
    # 시간 복잡도: 완전 이진트리의 최대 높이는 O(log(N))이므로
    # 반복하는(트리를 타고 내려가는) 최대 횟수도 O(log(N))이 된다.
    def delete1(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        max_pop = self.items.pop()
        parent_index = 1

        # 부모(바꿔 내려가야 하는 자신)이 리프 노드인지 검사
        # = 왼쪽 자식의 인덱스가 배열 범위를 벗어난 수면 본인이 리프 노드 맞음.
        while parent_index * 2 < len(self.items):
            left_child_index = parent_index * 2
            right_child_index = (parent_index * 2) + 1

            # 왼쪽 자식이 오른 자식이나 본인보다 더 크면 자리 바꾸기
            if self.items[left_child_index] >= self.items[right_child_index] \
                and self.items[left_child_index] > self.items[parent_index]:
                self.items[left_child_index], self.items[parent_index] = \
                self.items[parent_index], self.items[left_child_index]

                parent_index = left_child_index

            # 오른쪽 자식이 왼 자식이나 본인(부모)보다 더 크면 자리 바꾸기
            elif self.items[left_child_index] < self.items[right_child_index] \
                and self.items[right_child_index] > self.items[parent_index]:
                self.items[right_child_index], self.items[parent_index] = \
                self.items[parent_index], self.items[right_child_index]

                parent_index = right_child_index

        return max_pop, self.items  # 8 을 반환해야 합니다.


    # 강의판 해답: 신박한 방법이다. max_index라는 제 3의 인덱스를 만들어 놓고
    # '부모(나)', '왼쪽 자식', '오른쪽 자식' 셋 중 가장 큰 쪽을 이 값으로 한다.
    # 그리고 '부모(나)'가 지금 max_index라면 그냥 탈출(멈춤),
    # 그게 아니라면 그냥 max_index와 지금 인덱스(부모(나)의 인덱스)를 기반으로 교체!
    def delete2(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete1())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]