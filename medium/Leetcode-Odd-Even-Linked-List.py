# Problem: Odd Even Linked List
# Platform: LeetCode
# Difficulty: Medium
# Link: https://leetcode.com/problems/odd-even-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd = head
        even = odd.next
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenhead
        return head

head = listToLinkedList([2,1,3,5,6,4,7])
sol = Solution()
result = sol.oddEvenList(head)
print(linkedListToList(result))