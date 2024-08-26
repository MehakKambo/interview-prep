class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = set(nums)
        # longest = 0

        # for n in nums:
        #     if (n - 1) not in nums:
        #         length = 0

        #         while (n + length) in nums:
        #             length += 1

        #         longest = max(length, longest)

        # return longest
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        if len(nums) == 1:
            return 1
        longest = 1
        current = 1
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        return longest