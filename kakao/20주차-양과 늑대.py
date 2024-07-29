def solution(info, edges):
    def dfs(sheep, wolf, possible_nodes):
        nonlocal max_sheep
        # 양의 수가 최대일 때 갱신
        max_sheep = max(max_sheep, sheep)

        # 가능한 다음 노드에서 DFS
        for node in possible_nodes:
            next_possible_nodes = possible_nodes.copy()
            next_possible_nodes.remove(node)
            next_possible_nodes.extend(children[node])

            if info[node] == 0:
                # 현재 노드가 양일 경우
                dfs(sheep + 1, wolf, next_possible_nodes)
            else:
                # 현재 노드가 늑대일 경우
                if sheep > wolf + 1:
                    dfs(sheep, wolf + 1, next_possible_nodes)

    # 각 노드의 자식 노드를 저장하는 리스트
    children = [[] for _ in range(len(info))]
    for parent, child in edges:
        children[parent].append(child)

    max_sheep = 0
    # 루트 노드에서 시작 (양 1마리, 늑대 0마리)
    dfs(1, 0, children[0])
    return max_sheep
