from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n

        def dfs(point):
            if color[point] > 0:
                return color[point] == 2
            color[point] = 1
            for p in graph[point]:
                if not dfs(p):
                    return False
            color[point] = 2
            return True

        return [i for i in range(n) if dfs(i)]
