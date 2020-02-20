class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        for i in range(len(s)):
            if (len(s) - i) * 2 < right - left - 1:
                break
            l, r = i, i
            while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l > right - left:
                left = l
                right = r
            l, r = i + 1, i
            while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l > right - left:
                left = l
                right = r
        return s[left:right + 1]
            
