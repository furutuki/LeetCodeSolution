from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.height = [1 for i in range(n)]
        self.count = n

        for i in self.parent:
            self.parent[i] = i

    def find(self, num: int):
        if num == self.parent[num]:
            return num
        else:
            self.parent[num] = self.find(self.parent[num])
            return self.parent[num]

    def union(self, p: int, q: int):
        pp = self.find(p)
        qp = self.find(q)
        if pp != qp:
            if self.height[pp] > self.height[qp]:
                self.parent[qp] = pp
            elif self.height[qp] > self.height[pp]:
                self.parent[pp] = qp
            else:
                self.parent[pp] = qp
                self.height[qp] += 1
            self.count -= 1

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def getcount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        unionfind = UnionFind(m * n + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    unionfind.union(i * n + j, m * n)
                else:
                    if i + 1 < m and grid[i + 1][j] == '1':
                        unionfind.union((i + 1) * n + j, i * n + j)
                    if j + 1 < n and grid[i][j + 1] == '1':
                        unionfind.union(i * n + j + 1, i * n + j)

        return unionfind.getcount() - 1

s = Solution()
print(s.numIslands( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
))