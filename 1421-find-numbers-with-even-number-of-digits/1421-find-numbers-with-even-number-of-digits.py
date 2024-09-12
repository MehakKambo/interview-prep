class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # even_counter = 0
        # for num in nums:
        #     num_str = str(num)
        #     if (len(num_str) % 2 == 0):
        #         even_counter += 1
        
        # return even_counter

        even_counter = 0
        for num in nums:
            digit_count = 0
            while num > 0:
                num //= 10
                digit_count += 1
            if digit_count % 2 == 0:
                even_counter += 1
        return even_counter