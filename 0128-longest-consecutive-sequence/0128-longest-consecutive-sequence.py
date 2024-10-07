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
        unique_nums = set(nums)

        longest_seq = 1

        for num in unique_nums:
            current_seq = 1
            if (num - 1) in unique_nums:
                continue

            while num + current_seq in unique_nums:
                current_seq += 1

            longest_seq = max(current_seq, longest_seq)

        return longest_seq