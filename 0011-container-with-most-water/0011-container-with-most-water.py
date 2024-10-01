class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water_stored = 0

        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            current_water_stored = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            most_water_stored = max(most_water_stored, current_water_stored)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return most_water_stored
