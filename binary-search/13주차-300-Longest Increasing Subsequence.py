class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # Each element is at least a subsequence of length 1 by itself

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The longest subsequence length is the max value in dp array
        return max(dp)
