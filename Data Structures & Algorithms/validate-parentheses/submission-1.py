class Solution:
    def isValid(self, s: str) -> bool:
        brackMap = {
            '}': '{', ')': '(', ']': '['
        }
        brackStack = []
        for char in s:
            if char not in brackMap:
                brackStack.append(char)
            else:
                if len(brackStack) == 0:
                    return False
                last_element = brackStack.pop()
                if last_element == brackMap[char]:
                    continue
                else:
                    return False
        if len(brackStack) !=0:
            return False
        return True