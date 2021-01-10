from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 定义上下左右四个方向
        m = len(maze)  # 获取矩阵大小
        n = len(maze[0])

        # 构造dfs函数，其返回值为bool值
        def dfs(m, n, maze, x, y, directions, destination):
            maze[x][y] = -1  # -1表示该点已经过遍历，防止循环
            # 如果坐标为终点坐标，返回True
            if x == destination[0] and y == destination[1]:
                return True

            res = False
            i, j = x, y  # 保存坐标值
            for dx, dy in directions:  # 对四个方向进行遍历
                x, y = i, j
                while 0 <= x + dx < m and 0 <= y + dy < n and (maze[x + dx][y + dy] == 0 or maze[x + dx][y + dy] == -1):
                    # 当x,y坐标合法，并且对应值为0或-1时
                    x = x + dx  # 继续前进，模拟小球的滚动过程
                    y = y + dy  # 其中0为空地，而-1为之前遍历过的空地

                if maze[x][y] != -1:  # 如果该点的值不为-1，即未遍历过
                    # 进行遍历，并对res和遍历结果取或
                    # 有True即为True
                    res = res or dfs(m, n, maze, x, y, directions, destination)

            return res  # 返回res

        return dfs(m, n, maze, start[0], start[1], directions, destination)


so = Solution()
print(so.hasPath([[0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0],
                  [1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0]],
                 start=[0, 4],
                 destination=[4, 4]))
