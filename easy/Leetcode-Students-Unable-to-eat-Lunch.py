# Problem: Numbers of Students Unable to eat Lunch
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        failed = 0
        while students and failed < len(students):
            if students[0] != sandwiches[0]:
                students = students[1:]+students[:1]
                failed += 1
            else:
                students.pop(0)
                sandwiches.pop(0)
                failed = 0
        return len(students)
    
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
sol = Solution()
print(sol.countStudents(students,sandwiches))