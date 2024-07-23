class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        missing, duplicated = -1, -1
        for num in range(1, len(nums)+1):
            if counter[num] == 0:
                missing = num
            elif counter[num] == 2:
                duplicated = num

        return [duplicated, missing]
