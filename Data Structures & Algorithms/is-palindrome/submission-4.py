class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            l_char = s[left].lower()
            r_char = s[right].lower()
            if not l_char.isalnum():
                left += 1
                continue
            if not r_char.isalnum():
                right -= 1
                continue
            if l_char != r_char:
                return False
            right -= 1
            left += 1
        return True