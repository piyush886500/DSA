"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map={}
        oldTemp=head
        newTemp=Node(-1)
        prev = newTemp
        head2=newTemp
        while oldTemp:
            newTemp=Node(oldTemp.val)
            map[oldTemp]=newTemp
            prev.next=newTemp
            prev=newTemp
            oldTemp=oldTemp.next

        head2=head2.next
        head3=head2
        while head:
            if head.random!=None:
                head2.random=map[head.random]
            head=head.next
            head2=head2.next
            
        return head3