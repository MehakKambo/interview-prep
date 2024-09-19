class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        # s_dict, t_dict = {}, {}

        # for i in range(len(s)):
        #     s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        #     t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        # return s_dict == t_dict

        if len(s) != len(t):
            return False

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for value in range(len(s_sorted)):
            if s_sorted[value] != t_sorted[value]:
                return False
        
        return True