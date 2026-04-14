from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        valDict = defaultdict(list)
        left, right = 0, 1
        valDict[s[left]] = [0]
        dupLen, maxLen = 1, 0
        while right < len(s):
            while len(valDict[s[right]]) != 0:
                valDict[s[left]] = []
                left += 1
                dupLen -= 1
            valDict[s[right]] = [right]
            dupLen += 1
            maxLen = max(maxLen, dupLen)
            right += 1

        return maxLen
            
            

