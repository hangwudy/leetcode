from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue_max = deque()
        self.queue = deque()

    def max_value(self) -> int:
        if self.queue_max:
            return self.queue_max[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        while self.queue_max and self.queue_max[-1] < value:
            self.queue_max.pop()
        self.queue_max.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        ans = self.queue[0]
        if ans == self.queue_max[0]:
            self.queue_max.popleft()
        self.queue.popleft()
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
