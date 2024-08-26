class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [24,12,4,1]
        # [24,12,8,6]

        result = [1] * len(nums)

        prefix, postfix = 1, 1

        # [1,2,3,4]
        # [1,1,1,1]
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        for k in range(len(nums) - 1, -1, -1):
            result[k] *= postfix
            postfix *= nums[k]

        return result