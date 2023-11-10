# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight( head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leng = 1 if head!= None else 0 
        cur = head
        while  cur.next!=None:
            prev = cur
            cur=cur.next
            leng+=1
        if head==None or head.next== None:
            return head
        else:
            for i in range(k%leng):
                cur = head
                while  cur.next!=None:
                    prev = cur
                    cur=cur.next
                prev.next=None
                cur.next = head
                head = cur
            return head
    a = ListNode()
    a.val = 1
    b = ListNode()
    b.val = 2
    a.next = b
    c = ListNode()
    c.val = 3
    b.next = c
    print(rotateRight(a,100))
            


        