# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def func(node):
            if node.next is None:
                return str(node.val)
            return func(node.next) + str(node.val)
        a = func(l1)
        b = func(l2)
        ans = str(int(a) + int((b)))[::-1]
        head = None
        for i in ans:
            if head is None:
                head = ListNode(int(i))
                temp = head
            else:
                temp.next = ListNode(int(i))
                temp = temp.next
        return head
        