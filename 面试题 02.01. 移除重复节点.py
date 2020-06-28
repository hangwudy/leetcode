class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        seen = set()
        seen.add(head.val)
        pos = head
        while pos.next:
            cur = pos.next
            if cur.val not in seen:
                pos = pos.next
                seen.add(cur.val)
            else:
                pos.next = pos.next.next
        return head
