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
        if not nums:
            return 0
        nums = sorted(set(nums))
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        return longest