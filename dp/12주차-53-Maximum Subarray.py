class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0]
        s = 0
        for num in nums:
            s += num
            arr.append(s)

        mi = arr[0]
        ans = None
        for i in range(1, len(arr)):
            if ans is None or arr[i] - mi > ans:
                ans = arr[i] - mi
            if arr[i] < mi:
                mi = arr[i]

        return ans
