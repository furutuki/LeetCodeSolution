from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lineOne = [1]
        lineTwo = [1, 1]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [lineOne]
        elif numRows == 2:
            return [lineOne, lineTwo]
        ans = [lineOne, lineTwo]
        for i in range(2, numRows):
            line = []
            lastLine = ans[i - 1]
            for j in range(i + 1):
                if j == 0 or j == i:
                    line.append(1)
                else:
                    line.append(lastLine[j - 1] + lastLine[j])
            ans.append(line)
        return ans


s = Solution()
print(s.generate(3))
