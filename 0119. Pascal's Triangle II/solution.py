from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        lastLine = [1, 1]
        for i in range(2, rowIndex + 1):
            line = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    line.append(1)
                else:
                    line.append(lastLine[j - 1] + lastLine[j])
            lastLine = line
        return line


s = Solution()
print(s.getRow(2))
