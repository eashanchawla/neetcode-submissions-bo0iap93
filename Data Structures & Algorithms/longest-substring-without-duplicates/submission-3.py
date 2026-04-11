class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        seen_dict = {}
        start, end = 0, 0
        max_substring_len = 0
        for i, char in enumerate(s):
            if char not in seen_dict:
                seen_dict[char] = i
                end = i
            else:
                #means that the chain was broken and a duplicate is found
                max_substring_len = max(max_substring_len, (end - start + 1))
                start = max(start, seen_dict[char] + 1)
                seen_dict[char] = i
                end = i
        return max(max_substring_len, (end - start + 1))