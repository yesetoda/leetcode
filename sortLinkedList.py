# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur  = head
        ls = []
        while cur!=None:
            ls.append(cur.val)
            cur = cur.next
        a = ListNode(ls[0])
        cur = a
        for i in ls[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return a
            