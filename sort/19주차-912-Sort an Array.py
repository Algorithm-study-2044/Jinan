class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(start, end):
            pivot = nums[randint(start, end)]
            while start <= end:
                while nums[start] < pivot:
                    start += 1
                while nums[end] > pivot:
                    end -= 1
                if start <= end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
            return start

        def qsort(start, end):
            if start >= end:
                return
            mid = partition(start, end)
            qsort(start, mid - 1)
            qsort(mid, end)

        qsort(0, len(nums)-1)
        return nums
