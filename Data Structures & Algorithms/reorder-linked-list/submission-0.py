# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1, l2 = head, slow.next
        slow.next = None
        
        current = l2
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        l1, l2 = head, previous

        while l2:
            templ1 = l1.next
            templ2 = l2.next

            l1.next = l2
            l2.next = templ1
            l1 = templ1
            l2 = templ2
        

