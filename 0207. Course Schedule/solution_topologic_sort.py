from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """顶点的入度"""
        d = [0 for _ in range(numCourses)]

        """入度为0的顶点集合"""
        s = []

        """计算所有顶点的入度"""
        for edge in prerequisites:
            d[edge[0]] += 1

        """记录一下入度为0的顶点集合"""
        for i in range(numCourses):
            if d[i] == 0:
                s.append(i)

        popped_v_cnt = 0

        while len(s) > 0:
            v = s.pop()
            popped_v_cnt += 1

            """从v出发的终点的入度-1"""
            for i in range(len(prerequisites) - 1, -1, -1):
                edge = prerequisites[i]
                if edge[1] == v:
                    d[edge[0]] -= 1
                    if d[edge[0]] == 0:
                        s.append(edge[0])
                    del prerequisites[i]

        return False if popped_v_cnt < numCourses else True
