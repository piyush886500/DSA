# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        curr = head
        while curr!=None:
            curr = curr.next
            count+=1
        count = count//2

        while count!=0:
            head=head.next
            count-=1

        return head
