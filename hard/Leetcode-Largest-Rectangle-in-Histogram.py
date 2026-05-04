# Problem: Largest Rectangle in Histogram
# Platform: LeetCode
# Difficulty: Hard
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int])->int:
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]

                if stack:
                    Width = i-stack[-1]-1
                else:
                    Width = i

                area = height * Width
                max_area = max(max_area,area)
            stack.append(i)
        return max_area

heights = [2,1,5,6,2,3]
sol = Solution()
print(sol.largestRectangleArea(heights))