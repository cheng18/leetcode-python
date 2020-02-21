class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == "-" or s != s[::-1]:
            return False
        return True

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         if s[0] == "-":
#             return False
#         for i in range(len(s) // 2):
#             if s[i] != s[-i - 1]:
#                 return False
#         return True
