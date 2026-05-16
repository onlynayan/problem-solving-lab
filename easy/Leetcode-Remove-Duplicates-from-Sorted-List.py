# Problem: Remove Duplicates from Sorted List
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

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
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

head = listToLinkedList([1,1,2,3,3])
sol = Solution()
result = sol.deleteDuplicates(head)
print(linkedListToList(result))