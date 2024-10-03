class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        output = set()
        for num in nums2:
            if num in nums1:
                output.add(num)

        return output