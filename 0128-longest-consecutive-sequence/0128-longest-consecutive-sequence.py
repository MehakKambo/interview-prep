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
        nums = set(nums)

        longest_streak = 1
        for num in nums:
            if (num - 1) not in nums:
                current_streak = 1
                while (num + current_streak) in nums:
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak