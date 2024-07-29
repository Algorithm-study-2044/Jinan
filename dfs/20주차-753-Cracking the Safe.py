class Solution:
    def crackSafe(n, k):
        # Function to generate De Bruijn sequence using backtracking
        def dfs(node):
            for x in range(k):
                neighbor = node + str(x)
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor[1:])
                    result.append(str(x))

        # Start with an initial node and build the result
        visited = set()
        result = []
        dfs("0" * (n - 1))

        # Add the starting node to complete the sequence
        return "".join(result) + "0" * (n - 1)
