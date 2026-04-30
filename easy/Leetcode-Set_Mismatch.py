# Problem: Set Mismatch
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/set-mismatch/

from typing import List

class Solution:
    def setMismatch(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n+1)

        for num in nums:
            freq[num] += 1
        duplicate = 0
        missing = 0
        for i in range(1, n+1):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i
        return [duplicate, missing]
    
nums = [1,2,2,4]
sol = Solution()
print(sol.setMismatch(nums))
