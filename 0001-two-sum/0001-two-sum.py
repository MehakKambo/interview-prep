class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]
        # hashMap = {}

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashMap:
        #         return [i, hashMap[complement]]
        #     hashMap[nums[i]] = i