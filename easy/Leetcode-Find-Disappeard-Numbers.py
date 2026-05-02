# Problem: Find All Disappeared Numbers
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n+1)

        for num in nums:
            freq[num] += 1
        
        arr = []

        for i in range(1,n+1):
            if freq[i] == 0:
                arr.append(i)
        return arr

nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))