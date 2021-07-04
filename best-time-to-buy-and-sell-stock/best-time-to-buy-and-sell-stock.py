class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=prices[-1]
        ans=0
        for r in range(len(prices)-1,-1,-1):
            ans=max(ans,maxx-prices[r])
            maxx=max(maxx,prices[r])
        return ans