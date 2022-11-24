# Q. 인접 리스트가 주어질 때, 모든 노드를 DFS 순서대로 방문하시오.

# DFS 는 탐색하는 원소를 최대한 깊게 따라가야 합니다.
# 이걸 다시 말하면 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고,
# 가장 마지막에 넣은 노드들만 꺼내서 탐색하면 됩니다.
#
# 가장 마지막에 넣은 노드들..? → 스택을 이용하면 DFS 를 재귀 없이 구현할 수 있습니다!
#
# 구현의 방법은 다음과 같습니다.
# 1. 루트 노드를 스택에 넣습니다.
# 2. 현재 스택의 노드를 빼서 visited 에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다.
# 4. 2부터 반복한다.
# 5. 스택이 비면 탐색을 종료한다. => 중간에도 스택이 빌 때가 있는 것 같은데
#               => 그렇다 해도 while문을 벗어나기 전에 다시 스택에 내용물이 채워지게 된다.
#               => 참고로 중간에 스택이 비워졌다는 것은 끝 가지에 다다라서 진행중이라는 얘기가 된다.


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 인접 노드들이 [2, 5, 9]가 있다면, 거꾸로 9부터 스택에 넣어주는 방식으로 하면
# 강의와 반대되게 오름차순 순서로 방문해낼 수 있을 것 같다.
# 우선은 강의대로 [2, 5, 9]의 순서대로 넣어보고 잘 되면 반대로 해보자.
def dfs_stack1(adjacent_graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)

    while len(stack) != 0:
        visited.append(stack.pop())
        adjacent_nodes = adjacent_graph[visited[-1]]
        for node in adjacent_nodes[::-1]:
            if node not in visited:
                stack.append(node)
    # visited.append(stack.pop())
    # adjacent_nodes = adjacent_graph[visited[-1]]
    # for node in adjacent_nodes:
    #     ...# 반복의 시작과 끝 찾음!

    return visited


# 강의판 해답:
def dfs_stack2(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited


print(dfs_stack1(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!