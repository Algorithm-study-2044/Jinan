class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(index):
            nonlocal count
            if index == len(nums):
                return

            for i in range(index, len(nums)):
                num = nums[i]
                # Check if we can add nums[i] to the current subset
                if (num - k) not in used and (num + k) not in used:
                    used[num] += 1
                    count += 1
                    backtrack(i + 1)
                    used[num] -= 1
                    if used[num] == 0:
                        del used[num]

        nums.sort()
        used = defaultdict(int)
        count = 0
        backtrack(0)
        return count