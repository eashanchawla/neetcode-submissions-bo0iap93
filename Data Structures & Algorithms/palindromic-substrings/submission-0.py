class Solution:
    def expand(self, s: str, left: int, right: int) -> int:
        counter = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            counter += 1
            left -= 1
            right += 1
        return counter

    def countSubstrings(self, s: str) -> int:
        num_palinds = 0
        for i in range(len(s)):
            num_palinds += self.expand(s, i, i)
            num_palinds += self.expand(s, i, i + 1)
        return num_palinds
