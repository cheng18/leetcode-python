class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in d:
                if stack and d[c] == stack.pop():
                    continue
                else:
                    return False
            stack.append(c)
        return stack == []
