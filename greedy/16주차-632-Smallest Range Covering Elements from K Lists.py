class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        # Min-heap to store elements as (value, list_index, element_index)
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        smallest_range = [float('-inf'), float('inf')]
        
        # Process the heap
        while min_heap:
            min_val, list_idx, element_idx = heapq.heappop(min_heap)
            
            # Update the smallest range if the current range is smaller
            if current_max - min_val < smallest_range[1] - smallest_range[0] or \
               (current_max - min_val == smallest_range[1] - smallest_range[0] and min_val < smallest_range[0]):
                smallest_range = [min_val, current_max]
            
            # If the current list is exhausted, break the loop
            if element_idx + 1 == len(nums[list_idx]):
                break
            
            # Get the next element from the same list and add it to the heap
            next_val = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
            current_max = max(current_max, next_val)
        
        return smallest_range