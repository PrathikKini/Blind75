# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []
class ListNode:
    def __init__(self,next=None):
        self.next = next

class Solution:
    def singlelinkedlist(self,head: ListNode):
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev