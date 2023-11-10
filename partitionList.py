# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition( head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = []
        right = []
        cur = head
        while cur!=None :
            v=  cur.val
            if v>=x:
                right.append(v)
            else:
                left.append(v)
            if cur.next!=None:cur = cur.next
            else:break
            
        a= ListNode(left[0])
        cur = a
        for i in left[1:]+right:
            cur.next = ListNode(i)
            cur = cur.next
            print(i)
        return a
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(2)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(2)
    # a.next.next.next.next.next.next = ListNode(4)
    # a.next.next.next.next.next.next.next = ListNode(4)
    # a.next = ListNode(4)
    print(p := partition(a,3))
    c = p
    while  c!=None:
        print(c.val)
        c = c.next