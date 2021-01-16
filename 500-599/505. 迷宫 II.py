from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(maze)
        n = len(maze[0])
        distance = [[float('inf')] * n for _ in range(m)]
        distance[start[0]][start[1]] = 0
        queue = [(start[0], start[1])]
        while queue:
            i, j = queue.pop(0)
            # if i == destination[0] and j == destination[1]:
            #     return distance[i][j]
            for dx, dy in directions:
                x, y, step = i + dx, j + dy, distance[i][j] + 1,
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += dx
                    y += dy
                    step += 1
                x -= dx
                y -= dy
                step -= 1

                if distance[x][y] > step:
                    maze[x][y] = -1
                    distance[x][y] = step
                    queue.append((x, y))
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float(
            'inf') else -1


so = Solution()
print(so.shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                          [0, 4],
                          [4, 4]))
