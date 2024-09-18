class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        jewels = set(jewels)
        for stone in stones:
            if stone in jewels:
                counter += 1
        return counter