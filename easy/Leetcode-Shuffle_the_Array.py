# Problem: shuffle-the-array
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not nums:
            return ""

        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
    
nums = [2,5,1,3,4,7]
n = 3
sol = Solution()
print(sol.shuffle(nums, n))
