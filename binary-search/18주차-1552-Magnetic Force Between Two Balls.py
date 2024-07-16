class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the basket positions
        position.sort()

        # Helper function to check if we can place m balls with at least min_force apart
        def canPlaceBalls(min_force):
            count = 1  # Place the first ball in the first basket
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        # Binary search for the maximum minimum force
        left, right = 1, position[-1] - position[0]
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best
