class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Optimal Solution O(n)-time, O(1)- Space
        # result = 0 #gloabl max area
        # l, r = 0, len(height) - 1
        # while l < r:
        #     area = (r - l) * min(height[l], height[r])
        #     result = max(result, area)
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return result
        

        maxA = 0
        area = 0

        left, right = 0, len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxA = max(maxA, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxA