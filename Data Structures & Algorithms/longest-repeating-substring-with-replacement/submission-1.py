class Solution:
    def find_max(self, d):
        return max(d.values()) if d else 0


    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        count_dict = defaultdict(int)
        largest_substring = 0
        while start <= end and end < len(s):
            count_dict[s[end]] += 1
            current_substring_length = end - start + 1
            max_count = self.find_max(count_dict)
            print(current_substring_length, max_count, k)
            if current_substring_length - max_count > k:
                # shrink
                count_dict[s[start]] -= 1
                start += 1
            
            largest_substring = max(largest_substring, (end - start + 1))
            end += 1
        return largest_substring
