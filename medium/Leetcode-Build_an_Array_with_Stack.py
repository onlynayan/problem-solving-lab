# Problem: Build an Array with Stack Operation
# Platform: LeetCode
# Difficulty: Medium
# Link: https://leetcode.com/problems/build-an-array-with-stack-operations/description/

from typing import List

class Solution:
    def buildArray(self, target:List[int], n:int) -> List[str]:
        result = []
        j = 0

        for i in range(1,n+1):
            result.append('Push')

            if (i == target[j]):
                j+=1
            else:
                result.append("Pop")
            
            if (j == len(target)):
                break
        
        return result
    
target = [1,3]
n = 3
sol = Solution()
print(sol.buildArray(target, n))