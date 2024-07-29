class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_tank += gas[i] - cost[i]

            # If current_tank < 0, we cannot start from `start`
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        # If total gas is greater than or equal to total cost, return start index
        return start if total_gas >= total_cost else -1
