# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = head
        dummy.next = prev
        cur = head
        while cur:
            if cur.val!=0:
                cur = cur.next
            else:
                prev= cur
                while cur and cur.val!=0:
                    cur = cur.next
                while cur and cur.val==0:
                    cur = cur.next
                prev.next = cur
                prev = cur
        return dummy.next