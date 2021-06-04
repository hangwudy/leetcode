# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        tmp = headA
        while tmp:
            visited.add(tmp)
            tmp = tmp.next

        tmp = headB
        while tmp:
            if tmp in visited:
                return tmp
            tmp = tmp.next

        return None
