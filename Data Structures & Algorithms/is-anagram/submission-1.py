class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter 

        s_counter, t_counter = Counter(s), Counter(t)
        for key in s_counter.keys():
            if s_counter[key] != t_counter[key]:
                return False
        for key in t_counter.keys():
            if s_counter[key] != t_counter[key]:
                return False
        return True