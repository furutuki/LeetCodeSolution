from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque()
        q.append(0)
        while q:
            room = q.pop()
            visited.add(room)
            keys = rooms[room]
            for key in keys:
                if not visited.__contains__(key):
                    q.append(key)

        return len(visited) == len(rooms)
