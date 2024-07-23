class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def is_connected(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)


def is_reachable_from_origin(rect):
    x1, y1, x2, y2 = rect
    return (x1 == 0 or x2 == 0) and (y1 <= 0 <= y2) or (y1 == 0 or y2 == 0) and (x1 <= 0 <= x2)


def find_min_pu_commands(rectangles):
    N = len(rectangles)
    uf = UnionFind(N)
    reachable_from_origin = False

    for i in range(N):
        if is_reachable_from_origin(rectangles[i]):
            reachable_from_origin = True

        for j in range(i + 1, N):
            if is_connected(rectangles[i], rectangles[j]):
                uf.union(i, j)

    roots = set(uf.find(i) for i in range(N))
    num_components = len(roots)

    if reachable_from_origin:
        num_components -= 1

    return num_components


# 입력
N = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 계산 및 출력
print(find_min_pu_commands(rectangles))
