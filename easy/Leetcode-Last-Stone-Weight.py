# Problem: Last Stone Weight
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones:List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while (len(heap)>1):
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y!=x:
                heapq.heappush(heap, -(y-x))
        return -heap[0] if heap else 0

stones = [2,7,4,1,8,1]
sol = Solution()
print(sol.lastStoneWeight(stones))
