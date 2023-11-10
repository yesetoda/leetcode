# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList( head: Optional[ListNode]) -> None:
        cur = head
        nxt_temp = None
        lst=[]
        while cur.next.next!= None:
            nxt = cur.next.next.val
            cur.next.next=cur.next
        """
        Do not return anything, modify head in-place instead.
        """
        