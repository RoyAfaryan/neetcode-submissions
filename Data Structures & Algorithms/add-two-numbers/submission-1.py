# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Logic:
        # 1. traverse each list individually
        # 2. Store nums into a string
        # 3. Reverse each string
        # 4. Convert to int
        # 5. Do the math

        curr_l1, curr_l2 = l1, l2
        str_l1, str_l2 = "", ""

        while curr_l1 or curr_l2:
            if curr_l1:
                str_l1 += str(curr_l1.val)
                curr_l1 = curr_l1.next
            if curr_l2:
                str_l2 += str(curr_l2.val)
                curr_l2 = curr_l2.next

        val = str(int(str_l1[::-1]) + int(str_l2[::-1]))[::-1]

        head = ListNode()
        curr = head

        for c in val:
            curr.next = ListNode(int(c))
            curr = curr.next
            

        return head.next
