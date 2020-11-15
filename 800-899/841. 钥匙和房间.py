from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x):
            vis.add(x)
            nonlocal num
            num += 1
            for i in rooms[x]:
                if i not in vis:
                    dfs(i)

        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n


if __name__ == '__main__':
    so = Solution()
    print(so.canVisitAllRooms([[1], [2], [3], []]))
