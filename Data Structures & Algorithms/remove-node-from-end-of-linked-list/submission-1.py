# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            fast =head
            slow = head
            for i in range(n):
                if fast is None:
                    return
                fast = fast.next
            if fast == None:
                head = head.next
                return head
            while (fast.next != None):
                slow = slow.next
                fast = fast.next
            if slow.next != None:
                slow.next = slow.next.next
            return head
        