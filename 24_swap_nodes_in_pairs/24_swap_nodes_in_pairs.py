# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(head):
            if head.next:
                temp = ListNode(0, head.next)
                if temp.next.next:
                    head.next = swap(temp.next.next)
                else:
                    head.next = None
                temp.next.next = head
                return temp.next
            else:
                return head
        if head:
            return(swap(head))
