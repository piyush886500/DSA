# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head1=list1
        head2=list2
        dummy = ListNode(0)
        prev = dummy
        while head1!=None and head2!=None:
            if head1.val <= head2.val:
                prev.next = head1
                head1=head1.next
            else:
                prev.next=head2
                head2=head2.next
            prev=prev.next
        if head1:
            prev.next=head1
        else:
            prev.next=head2
        return dummy.next

