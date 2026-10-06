# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head and head.val == val:
            head = head.next

        curr = head

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
    
            else:
                curr = curr.next

        return head