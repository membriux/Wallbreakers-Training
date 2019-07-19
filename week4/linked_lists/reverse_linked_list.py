# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        new = ListNode(head.val)
        while head.next:
            # 1st iteration
            prev = new  # previous head = 1
            new = ListNode(head.next.val) # new = 2
            new.next = prev # 2 -> 1

            head = head.next
        return new


            
