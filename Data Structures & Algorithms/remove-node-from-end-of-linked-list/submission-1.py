# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Logic:
        # 1. Go one pass to find length
        # 2. Subtract length by n 
        # 3. Go second pass 
        # 4. Replace node

        current = head
        length = 0

        while current:
            current = current.next
            length += 1

        node2Remove = length - n
        i = 0
        current = head
        previous = None

        while current:
            if i == node2Remove:
                if previous == None:
                    head = head.next
                    break
                previous.next = current.next
                break
            previous = current
            current = current.next
            i+=1

        return head

