from typing import List


class Solution:

    def dfs(self, d: dict,  src: str, ans: List[str]):
        if d.__contains__(src):
            dest_list = d[src]
            while dest_list and len(dest_list) > 0:
                next_city = dest_list[0]
                del dest_list[0]
                self.dfs(d, next_city, ans)
        ans.append(src)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        d = dict()
        for pair in tickets:
            if not d.__contains__(pair[0]):
                d[pair[0]] = list()
            d[pair[0]].append(pair[1])
            d[pair[0]].sort()

        ans = []
        self.dfs(d, "JFK", ans)
        ans.reverse()
        return ans
