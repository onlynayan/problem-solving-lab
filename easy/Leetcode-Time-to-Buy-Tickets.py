# Problem: Time Needed to Buy Tickets
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/time-needed-to-buy-tickets/

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0 
        for i in range(len(tickets)):
            if (i<=k):
                time += min(tickets[i],tickets[k])
            else:
                time += min(tickets[i], tickets[k]-1)
        return time
    
tickets = [5,1,1,1]
k = 0
sol = Solution()
print(sol.timeRequiredToBuy(tickets, k))