# Problem: Longest Common Prefix
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/description/


from typing import List

class Solution:
    def LongestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for s in strs:
                if (i>= len(s) or s[i]!=char):
                    return prefix

            prefix += char

        return prefix
    
    
strs = ["flower","flow","flight"]
sol = Solution()
result = sol.LongestCommonPrefix(strs)
print(result)