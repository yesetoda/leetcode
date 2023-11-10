# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.visited = False 

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur!=None:
            if cur.visited==True:
                return "tail connects to node index 0"
            else:
                cur.visited=True
            cur = cur.next
        return "no cycle"
    print()