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

        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)