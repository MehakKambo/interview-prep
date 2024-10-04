class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [24,12,4,1]
        # [24,12,8,6]

        # result = [1] * len(nums)

        # prefix, postfix = 1, 1

        # # [1,2,3,4]
        # # [1,1,1,1]
        # for i in range(len(nums)):
        #     result[i] = prefix
        #     prefix *= nums[i]

        # for k in range(len(nums) - 1, -1, -1):
        #     result[k] *= postfix
        #     postfix *= nums[k]

        # return result

        # Step 1: Calculate the total product of all non-zero elements and count zeroes
        total_product = 1
        zero_count = 0

        # Calculate the product of non-zero elements and count zeroes
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        # Step 2: Handle different scenarios based on the number of zeroes
        result = [0] * len(nums)

        if zero_count > 1:
            # If more than one zero, all results will be zero
            return result

        for i, num in enumerate(nums):
            if zero_count == 1:
                # If exactly one zero, only the position of the zero should have the product of non-zero elements
                if num == 0:
                    result[i] = total_product
            else:
                # If no zero, use division to get the product except self
                result[i] = total_product // num

        return result
        