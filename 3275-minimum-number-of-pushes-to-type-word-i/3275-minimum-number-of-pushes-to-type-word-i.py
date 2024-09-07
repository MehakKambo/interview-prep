class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        else:
            q = n // 8
            r = n % 8
            res = 0
            for i in range(1, q + 1):
                res += i * 8
            res += r * (q + 1)
            return res