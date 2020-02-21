class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        ans = [[1]]
        for numRow in range(2, numRows + 1):
            temp = [1]
            for col in range(numRow - 2):
                temp.append(ans[-1][col] + ans[-1][col + 1])
            temp.append(1)
            ans.append(temp)
        return ans
