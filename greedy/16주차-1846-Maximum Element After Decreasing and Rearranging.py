class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize the first element to 1
        arr[0] = 1
        
        # Step 3: Adjust each subsequent element to ensure the conditions
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1] + 1:
                arr[i] = arr[i-1] + 1
        
        # Step 4: The maximum element in the adjusted array is the result
        return arr[-1]