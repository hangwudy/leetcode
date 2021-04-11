class Solution:
    def clumsy(self, N: int) -> int:
        stack = list()
        index = 0
        stack.append(N)
        N -= 1
        while N:
            if index % 4 == 0:
                stack.append(stack.pop() * N)
            elif index % 4 == 1:
                stack.append(int(stack.pop() / N))
            elif index % 4 == 2:
                stack.append(N)
            else:
                stack.append(-N)
            index += 1
            N -= 1
        return sum(stack)
