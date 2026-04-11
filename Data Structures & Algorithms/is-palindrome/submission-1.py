class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean = ''.join(char for char in s if char.isalnum()).lower()
        # return clean == clean[::-1]

        start, end = 0, len(s) - 1
        while start < end:
            start_alpha = s[start].lower()
            end_alpha = s[end].lower()
            if not start_alpha.isalnum():
                start += 1
                continue
            if not end_alpha.isalnum():
                end -= 1
                continue
            if start_alpha == end_alpha:
                start += 1
                end -= 1
            else:
                return False
        return True
