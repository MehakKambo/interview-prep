class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1,2,2,3,5,6], m = 3
        #        w
        # [1,2,3]
        #      p1 
        # [2,5,6]
        #    p2

        nums1_copy = nums1[:m]
        
        p1, p2 = 0, 0
        
        for p in range(n+m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
                
