# Problem: Final Prices with a Special Discount in a shop
# Platform: LeetCode
# Difficulty: Easy
# Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0]*n
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break
                else:
                    ans[i] = prices[i]
        ans[n-1] = prices[n-1]
        return ans
    
prices = [8,4,6,2,3]
sol = Solution()
print(sol.finalPrices(prices))