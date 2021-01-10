# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head.next
        pre = head
        while cur is not None:
            if cur.val == pre.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return head
