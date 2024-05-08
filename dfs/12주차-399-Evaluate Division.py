from collections import defaultdict, deque


class Solution:

    def find_ratio(self, start, end, visited, ratio=1.0):
        if start == end:
            return ratio

        if start not in visited:
            visited.add(start)
            for weight, curr in self.G[start]:
                res = self.find_ratio(curr, end, visited, ratio * weight)
                if res is not None:
                    return res

        return None

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.G = defaultdict(set)
        for e, v in zip(equations, values):
            self.G[e[0]].add((v, e[1]))
            self.G[e[1]].add((1/v, e[0]))

        ans = []
        for q in queries:
            if q[0] not in self.G or q[1] not in self.G:
                ans.append(-1.0)
            else:
                ratio = self.find_ratio(q[0], q[1], set())
                ans.append(ratio if ratio is not None else -1.0)
        return ans
