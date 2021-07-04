class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
            x=prices[i]-prices[i-1]
            if x>0:
                ans+=x
        return ans
        