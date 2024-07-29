class Solution:
    def twoCitySchedCost(costs):
        # Sort the list by the difference in cost between city A and city B
        costs.sort(key=lambda x: x[0] - x[1])

        total_cost = 0
        n = len(costs) // 2

        # Assign the first half to city A and the second half to city B
        for i in range(n):
            total_cost += costs[i][0]  # Assign first n people to city A
        for i in range(n, 2*n):
            total_cost += costs[i][1]  # Assign next n people to city B

        return total_cost
