class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Function to check if we can split the array into <= k subarrays with max subarray sum <= max_sum
        def canSplit(nums, max_sum, k):
            current_sum = 0
            splits = 1
            for num in nums:
                if current_sum + num > max_sum:
                    splits += 1
                    current_sum = num
                    if splits > k:
                        return False
                else:
                    current_sum += num
            return True

        # Binary search range
        left, right = max(nums), sum(nums)

        while left <= right:
            mid = (left + right) // 2
            if canSplit(nums, mid, k):
                right = mid - 1
            else:
                left = mid + 1

        return left
