# Problem: Exclusive Time of Functions
# Platform: LeetCode
# Difficulty: Medium
# Link: https://leetcode.com/problems/exclusive-time-of-functions

from typing import List

class Solution:
    def exclusiveTime(self, n:int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0]*n
        prev_time = 0

        for log in logs:
            func_id, status, time = log.split(":")
            func_id = int(func_id)
            time = int(time)

            if status == "start":
                if stack:
                    ans[stack[-1]] += time-prev_time

                stack.append(func_id)
                prev_time = time
            
            else:
                ans[stack.pop()] += time-prev_time+1
                prev_time = time+1
        return ans
    
n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
sol = Solution()
print(sol.exclusiveTime(n,logs))