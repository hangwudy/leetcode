class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        r = result
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            if carry > 0:
                r.next = ListNode(1)
        return result.next


solution = Solution()
re = solution.addTwoNumbers(ListNode(3), ListNode(2))
print(re.val)

from collections import defaultdict

ans = defaultdict(int)

print(ans[1])
print(ans)
