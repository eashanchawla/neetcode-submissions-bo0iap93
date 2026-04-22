class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {
            ')': '(', '}': '{', ']': '['
        }
        stack = []

        for i, char in enumerate(s):
            if char not in pmap:
                stack.append(char)
            else:
                if not stack: return False
                last_elem = stack.pop()
                if last_elem == pmap[char]:
                    continue
                else:
                    return False
        return True if len(stack) == 0 else False