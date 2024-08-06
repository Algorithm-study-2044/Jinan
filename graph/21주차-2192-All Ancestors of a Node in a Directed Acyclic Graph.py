class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 주의: dp를 여기서 초기화하지 않으면 주화입마에 빠질 수 있음!
        self.dp = {} 
        self.graph = defaultdict(set)
        for edge in edges:
            fr, to = edge
            self.graph[to].add(fr)
        return [self.helper(node) for node in range(n)]
    
    def helper(self, v) -> List[int]:
        if v in self.dp:
            return self.dp[v]
        
        res = set()
        for parent in self.graph[v]:
            res.add(parent)
            res |= set(self.helper(parent))

        res = sorted(list(res))
        self.dp[v] = res
        return res

        