from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)-1):
                left = account[i]
                right = account[i+1]
                graph[left].add(right)
                graph[right].add(left)

        visited = set()

        def dfs(v, emails):
            visited.add(v)
            emails.add(v)
            for v in graph[v]:
                if v not in emails:
                    dfs(v, emails)
            return emails

        res = []
        for account in accounts:
            name = account[0]
            root = account[1]
            if root in visited:
                continue
            res.append([name, *sorted(list(dfs(root, set())))])

        return res
