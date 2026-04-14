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
        maxLen = 0
        while right < len(s):
            # check where the duplicate is 
            if len(valDict[s[right]]) != 0:
                left = max(left, valDict[s[right]][0] + 1)
            # while len(valDict[s[right]]) != 0:
            #     valDict[s[left]] = []
            #     left += 1

            valDict[s[right]] = [right]

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
            
            

