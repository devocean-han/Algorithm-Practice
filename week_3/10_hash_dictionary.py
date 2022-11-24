# 해쉬는 곧 딕셔너리라고 볼 수 있다.
# '키'를 넣으면 O(1)의 시간 안에, 즉 곧바로 '값'을 찾아낼 수 있는 자료구조이다.
# 파이썬의 딕셔너리는 내부적으로 리스트를 사용하는데...

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!