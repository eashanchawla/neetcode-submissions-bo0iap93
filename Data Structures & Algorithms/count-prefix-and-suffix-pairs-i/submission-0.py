class Solution:
    def isPrefix(self, a, b):
        return b[:len(a)] == a and b[-len(a):] == a
            
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefix(words[i], words[j]):
                    answer += 1
        return answer
        