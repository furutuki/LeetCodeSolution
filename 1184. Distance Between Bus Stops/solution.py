from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        sum = [0 for _ in range(n + 1)]
        for i in range(1, n, 1):
            sum[i] = distance[i - 1] + sum[i - 1]
        sum[n] = sum[n - 1] + distance[n - 1]
        if start > destination:
            start, destination = destination, start
        p = sum[destination] - sum[start]
        q = sum[n] - p
        return min(p,q)