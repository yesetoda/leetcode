# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle( head: Optional[ListNode]) -> bool:
        cur = head
        while cur!=None:
            if cur.val==10**5+1:
                return True
            else:
                cur.val = 10**5+1
            cur=cur.next
        return False
    a = ListNode(3)
    b= ListNode(2)
    a.next = b
    c= ListNode(0)
    b.next = c
    d = ListNode(-4)
    c.next =d
    d.next = b
    print(hasCycle(a))
# from random import randint
# print([randint(-10**5,10**5) for i in range(10**4)])