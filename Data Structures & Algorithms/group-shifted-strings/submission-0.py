from collections import defaultdict
class Solution:
    def calculate_gaps(self, word: str):
        if len(word) == 1:
            return ()
        gaps = list()
        for i in range(1, len(word)):
            diff = ord(word[i]) - ord(word[i - 1])
            gaps.append(diff % 26)
        return tuple(gaps)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        gapDict = defaultdict(list)
        for word in strings:
            gap_tuple = self.calculate_gaps(word)
            gapDict[gap_tuple].append(word)
        return [x for x in gapDict.values()]