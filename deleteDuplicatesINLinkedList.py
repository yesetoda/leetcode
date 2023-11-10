from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(-101)
        dummy.next = head
        prev = dummy
        cur = head

        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                while cur.next is not None and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next


# Create the linked list
a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(2)
b.next = c
d = ListNode(3)
c.next = d

# Create an instance of the Solution class
solution = Solution()

# Call the deleteDuplicates method
result = solution.deleteDuplicates(a)

# Print the modified linked list
current = result
while current is not None:
    print(current.val)
    current = current.next