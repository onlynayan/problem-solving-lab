# Problem: Smaller than Current Numbers
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        count_map = {}

        for i, num in enumerate(arr):
            if num not in count_map:
                count_map[num] = i
        
        result = []
        for num in nums:
            result.append(count_map[num])
        
        return result
    
nums = [8,1,2,2,3]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))