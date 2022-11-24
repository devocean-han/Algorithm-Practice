# Q. 인접 리스트가 주어질 때, 모든 노드를 BFS 순서대로 방문하시오.

# 1. 시작 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
#
# 이 과정을 큐가 빌때까지 반복하면 됩니다!

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


# 내 해답: 힌트는 queue를 사용하라는 것.
def bfs_queue1(adj_graph, start_node):
    queue = [start_node]
    visited = [start_node]
    # 친구들을 주르륵 먼저 visited에 넣어 두고, 또 queue에도 넣는다. 그리고서
    # queue에 있는 애들을 차례로 꺼내서 그들의 친구들을 주르륵 불러내서 좌르륵 visited와 queue에 넣고...

    while queue:
        adjacent_nodes = adj_graph[queue.pop(0)]
        for node in adjacent_nodes:
            if node not in visited:
                visited.append(node)
                queue.append(node)
        # adjacent_nodes = adj_graph[queue.remove(0)]
        # for node in adjacent_nodes:
        #     if node not in visited:
        #         queue.append(node)
        #         visited.append(node)
        #         => 이만큼이 반복되는 시작과 끝!
    return visited


# 강의판 해답: => 어떻게 이게 동작하지? 친구들을 쫙 ... 아! queue에만 딱 순서대로 저장해두고,
# 정확히 queue에서 뽑힌 '자기 차례(친구들을 부르는 본인 노드)'가 되었을 때에야 visited에
# 들어가는 방식인 거구나..!
# DFS 의 stack 버전 때랑 똑같은데 이건 정말 방식이 낯설다...
def bfs_queue2(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


print(bfs_queue1(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!