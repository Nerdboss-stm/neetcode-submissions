class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
    
        for l in range(len(prices)):
            for j in range(l+1, len(prices)):
                diff = prices[j] - prices[l]
                if diff > res:
                    res = diff
        return res
            
            
            

        