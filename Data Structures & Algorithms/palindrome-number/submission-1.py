from copy import deepcopy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        x_original = deepcopy(x)
        reverse_string = ''
        while x > 0:
            rem = x % 10
            x = x // 10
            reverse_string += str(rem)
        
        return int(reverse_string) == x_original