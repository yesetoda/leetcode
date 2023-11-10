# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(l):
    reversedlinkedlist = l[::-1]
    return reversedlinkedlist
list = []
print(reverseList(list))