# 그래프를 DFS 방식으로 탐색하기. 재귀함수로. 

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
visited = []


# 내 버전: 1이 이미 visited에 들어있는 경우는 대응할 수 없다.
def dfs_recursion1(adjacent_graph, cur_node, visited_array):

    if cur_node not in visited_array:
        visited_array.append(cur_node)
        adjacents = adjacent_graph[cur_node]
        for num in adjacents:
            dfs_recursion1(adjacent_graph, num, visited_array)
            # if num not in visited_array:
            #     visited_array.append(num)
            #     adjacents = adjacent_graph[num]
            #     for num2 in adjacents:
            #         if num2 not in visited_array:
            #             visited_array.append(num2)
            #             ...
            #     ...
            # else: 를 해줄 것 없이 if가 모두 소모되고 나면 알아서 다음 for를 돌 것이다..
    return True


# 강의판 해답:
def dfs_recursion2(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion2(adjacent_graph, adjacent_node, visited_array)


dfs_recursion2(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!