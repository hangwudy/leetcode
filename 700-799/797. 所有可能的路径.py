from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        ans = list()
        stack = list()

        def dfs(x: int):
            if x == n - 1:
                ans.append(stack[::])
                return
            for y in graph[x]:
                stack.append(y)
                dfs(y)
                stack.pop()

        stack.append(0)
        dfs(0)
        return ans


so = Solution()
print(so.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
