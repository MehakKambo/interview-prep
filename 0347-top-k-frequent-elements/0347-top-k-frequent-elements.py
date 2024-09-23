class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time for this check
        # if k == len(nums):
        #     return nums
        
        # # 1. Build a frequency map: element -> frequency
        # # O(N) time
        # frequency_map = {}
        # for num in nums:
        #     if num in frequency_map:
        #         frequency_map[num] += 1
        #     else:
        #         frequency_map[num] = 1
        
        # # 2. Use a min-heap to keep track of top k elements
        # # O(N log k) time
        # min_heap = []
        
        # # Iterate over the frequency map
        # for num, freq in frequency_map.items():
        #     # Push the frequency and element as a tuple
        #     heapq.heappush(min_heap, (freq, num))
            
        #     # If the heap grows larger than k, pop the smallest element (min-heap behavior)
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # # 3. Extract the elements from the heap
        # # O(k) time
        # top_k_elements = [num for freq, num in min_heap]
        
        # return top_k_elements
        
        frequency_map = {}
        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)

        frequency_groups = [[] for i in range(len(nums) + 1)]
        # [[], [], [], []]
        for element, frequency in frequency_map.items():
            frequency_groups[frequency].append(element)

        top_k_elements = []
        for i in range(len(frequency_groups) - 1, 0, -1):
            for element in frequency_groups[i]:
                top_k_elements.append(element)
                if len(top_k_elements) == k:
                    return top_k_elements
