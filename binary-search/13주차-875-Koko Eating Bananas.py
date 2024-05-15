class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate the hours needed for a given speed
        def hours_required(speed):
            total_hours = 0
            for pile in piles:
                # Equivalent to math.ceil(pile / speed)
                total_hours += (pile + speed - 1) // speed
            return total_hours

        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2
            if hours_required(mid) <= h:
                high = mid  # Try a smaller speed
            else:
                low = mid + 1  # Increase speed

        return low
