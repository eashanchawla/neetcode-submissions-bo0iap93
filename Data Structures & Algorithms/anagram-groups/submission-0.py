from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for current_str in strs:
            str_tup = [0] * 26
            for current_char in current_str:
                str_tup[ord(current_char) - ord('a')] += 1
            hmap[tuple(str_tup)].append(current_str)
        return list(hmap.values())

