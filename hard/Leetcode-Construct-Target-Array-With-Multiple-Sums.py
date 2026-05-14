# Problem: Construct Target Array With Multiple Sums
# Platform: LeetCode
# Difficulty: Hard
# Link: https://leetcode.com/problems/construct-target-array-with-multiple-sums/

from typing import List
import heapq

class Solution:
    def isPossible(self, target:List[int])-> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)

        while(True):
            largest = -heapq.heappop(heap)
            others = total - largest

            if largest == 1 or others == 1:
                return True
            
            if others == 0 or largest<=others:
                return False
            
            prev = largest % others

            if prev == 0:
                return False

            total = prev + others
            heapq.heappush(heap, -prev)

target = [9,3,5]
sol = Solution()
print(sol.isPossible(target))