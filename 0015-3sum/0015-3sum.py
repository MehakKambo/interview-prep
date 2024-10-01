class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_triplets = []
        nums.sort()

        for index, current_number in enumerate(nums):
            if current_number > 0:
                break

            if index > 0 and current_number == nums[index - 1]:
                continue

            left_pointer = index + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                current_sum = current_number + nums[left_pointer] + nums[right_pointer]
                if current_sum > 0:
                    right_pointer -= 1
                elif current_sum < 0:
                    left_pointer += 1
                else:
                    result_triplets.append([current_number, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
        return result_triplets 