# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = list1
        current2 = list2
        head_merged = ListNode()
        current_merged = head_merged

        while current1 or current2:

            if current1 and current2:
                if current1.val >= current2.val:
                    current_merged.next = current2
                    current2 = current2.next
                else:
                    current_merged.next = current1
                    current1 = current1.next
            elif current1:
                current_merged.next = current1
                break
            elif current2:
                current_merged.next = current2
                break

            current_merged = current_merged.next

        return head_merged.next
