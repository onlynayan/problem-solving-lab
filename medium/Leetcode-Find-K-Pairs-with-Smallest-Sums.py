# Problem: Find K Pairs with Smallest Sums
# Platform: LeetCode
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1:List[int], nums2:List[int], k:int) -> List[List[int]]:
        heap = []
        result = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i]+nums2[0],i,0))
        
        while heap and len(result)<k:
            total,i,j = heapq.heappop(heap)

            result.append([nums1[i],nums2[j]])

            if j+1<len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return result

# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
sol = Solution()
print(sol.kSmallestPairs(nums1, nums2, k))