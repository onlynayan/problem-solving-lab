# Problem: Masking Personal Information
# Platform: LeetCode
# Difficulty: Medium
# Link: https://leetcode.com/problems/masking-personal-information/

class Solution:
    def maskPII(self, s:str)->str:
        if '@' in s:
            x = s.lower()
            name, domain = x.split('@')
            return name[0]+"*****"+name[-1]+'@'+domain
        else:
            digits = []
            for ch in s:
                if ch.isdigit():
                    digits.append(ch)

            digits = ''.join(digits)

            local = "***-***-"+digits[-4:]
            country_len = len(digits)-10
            if country_len == 0:
                return local
            return "+"+"*"*country_len+"-"+local

# s = "LeetCode@LeetCode.com"
s = "86-(10)12345678"
# s = "1(234)567-890"
sol = Solution()
print(sol.maskPII(s))