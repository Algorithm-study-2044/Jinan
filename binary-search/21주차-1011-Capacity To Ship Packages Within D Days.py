class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipWithCapacity(capacity: int) -> bool:
            current_load = 0
            required_days = 1
            
            for weight in weights:
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = 0
                    if required_days > days:
                        return False
                current_load += weight
            
            return True
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShipWithCapacity(mid):
                right = mid
            else:
                left = mid + 1
        
        return left