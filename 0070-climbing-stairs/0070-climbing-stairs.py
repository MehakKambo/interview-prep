class Solution:
    def climbStairs(self, n: int) -> int:

        # if n == 0:
        #     return 0
        
        # if n == 1:
        #     return 1
        
        # if n == 2:
        #     return 2
        # k = self.climbStairs(n - 1) 3
        # m = self.climbStairs(n - 2) 2
        # return k + m

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp

        return one