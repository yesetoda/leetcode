# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        out_list = []
        for i in lists:
            out_list.append(i.val)
            cur = i
            while cur.next!=None:
                cur= cur.next
                out_list.append(cur.val)
        print(out_list)