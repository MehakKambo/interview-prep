class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = [False] * len(candies)

        greatest_num_candies = max(candies)

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= greatest_num_candies:
                output[i] = True
            
        
        return output