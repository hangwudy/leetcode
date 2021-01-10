# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        p = head
        while p is not None:
            if p in seen:
                return True
            seen.add(p)
            p = p.next
        return False
