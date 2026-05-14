# Problem: License Key Formatting
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/license-key-formatting/

from typing import List

class Solution:
    def licenseKeyFormatting(self, s:str, k:int) -> str:
        s = s.replace("-","").upper()
        result = []

        while(len(s)>k):
            result.append(s[-k:])
            s = s[:-k]
        
        if s:
            result.append(s)
        
        result.reverse()

        return "-".join(result)

s = "5F3Z-2e-9-w"
k = 4
sol = Solution()
print(sol.licenseKeyFormatting(s,k))