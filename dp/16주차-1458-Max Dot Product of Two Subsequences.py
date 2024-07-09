class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                product = nums1[i] * nums2[j]
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + product)
                dp[i][j] = max(dp[i][j], product)
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        return dp[m-1][n-1]