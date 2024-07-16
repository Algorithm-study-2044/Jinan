class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        # Create adjacency list and in-degree list
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        
        # Initialize the queue with courses having no prerequisites
        queue = deque()
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
                dp[i] = time[i - 1]
        
        # Process the courses in topological order
        while queue:
            current = queue.popleft()
            current_time = dp[current]
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                
                # Update the dp for the neighbor course
                dp[neighbor] = max(dp[neighbor], current_time + time[neighbor - 1])
        
        # The answer is the maximum time needed to complete any course
        return max(dp)