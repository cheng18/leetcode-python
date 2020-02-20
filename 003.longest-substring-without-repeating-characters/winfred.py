class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i - start + 1)
        return ans


class Solution: # Slow
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 0
        for i in range(len(s)):
            j = i + 1
            if j + ans > len(s):
                break
            st = s[i]
            while j < len(s) and s[j] not in st:
                st += s[j]
                j += 1
            ans = max(ans, len(st))
        return ans
