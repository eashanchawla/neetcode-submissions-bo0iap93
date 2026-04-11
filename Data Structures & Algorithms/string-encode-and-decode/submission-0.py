class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) +'#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []
        while True:

            try:
                num = ''
                # Try to find the length of the upcoming string
                while s[i] != '#':
                    num += s[i]
                    i += 1 
                length_of_string = int(num)
                j = 1
                if s[i] =='#':
                    if length_of_string == 0:
                        decoded_list.append('')
                        i = i + 1
                    else:
                        start, end = i + 1, i + 1 + length_of_string
                        decoded_list.append(s[start: end])
                        i = end
            except Exception as e:
                pass
            finally:
                if i >= len(s):
                    break
        return decoded_list 