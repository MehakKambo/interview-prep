class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the result triplets
        result_triplets = []

        # Sort the input array to easily find and skip duplicates
        nums.sort()

        # Iterate through the array to select each element as the first number in the triplet
        for index, current_number in enumerate(nums):
            # If the current number is greater than 0, break the loop as no triplet can sum to 0 beyond this point
            if current_number > 0:
                break
            
            # Skip duplicate values to avoid repeating the same triplet in the result
            if index > 0 and current_number == nums[index - 1]:
                continue

            # Initialize two pointers for the second and third elements of the triplet
            left_pointer, right_pointer = index + 1, len(nums) - 1

            # Use a two-pointer technique to find the remaining two numbers
            while left_pointer < right_pointer:
                # Calculate the sum of the current triplet
                current_sum = current_number + nums[left_pointer] + nums[right_pointer]

                # If the sum is greater than 0, move the right pointer to decrease the sum
                if current_sum > 0:
                    right_pointer -= 1
                # If the sum is less than 0, move the left pointer to increase the sum
                elif current_sum < 0:
                    left_pointer += 1
                else:
                    # If the sum is zero, add the current triplet to the result
                    result_triplets.append([current_number, nums[left_pointer], nums[right_pointer]])

                    # Move both pointers inward to find new triplets
                    left_pointer += 1
                    right_pointer -= 1

                    # Skip duplicate values for the second element of the triplet
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1

        # Return the list of all unique triplets that sum to zero
        return result_triplets
