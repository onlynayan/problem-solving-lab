# Problem: Implement Queue using Stacks
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/repeated-substring-pattern/

# First Approach
class Solution:
    def repeatedSubstringPattern(self, s:str)->bool:
        return s in (s+s)[1:-1] #pattern match, string rotation

# Second Approach
# class Solution:
#     def repeatedSubstringPattern(self, s:str)->bool:
#         n = len(s)

#         for i in range(1,(n//2)+1):
#             if (n%i == 0):
#                 sub = s[:i]
#                 repeated = sub*(n//i)

#                 if repeated == s:
#                     return True
#         return False

#TestCase
# s = "abcabcabcabc"
# s = "maximmaxim"
s = "maximaxim"
sol = Solution()
print(sol.repeatedSubstringPattern(s))