# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(l1, l2):
        num1 = ""
        num2 = ""
        for i,j in zip(l1,l2):
            num1+=str(i)
            num2+=str(j)
        sum = str(int(num1[::-1])+int(num2[::-1]))[::-1]
        out = []
        for i in sum:
            out.append(i)
        return out
    l1 = [9,9,9,9,9,9,9]
    l2 =[9,9,9,9]
    print(addTwoNumbers(l1,l2))