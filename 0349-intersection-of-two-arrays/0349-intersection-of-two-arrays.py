class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        output = []
        for num in nums2:
            if num in nums1:
                output.append(num)
                nums1.remove(num)
        return output