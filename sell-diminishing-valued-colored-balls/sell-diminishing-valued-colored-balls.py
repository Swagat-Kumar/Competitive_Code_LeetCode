class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def getSum(start,end):
            return start*(start+1)//2-end*(end+1)//2
        inventory.sort(reverse=True)
        factor=1
        n=len(inventory)
        i=0
        ans=0
        while orders>0:
            if i<n-1 and inventory[i]>inventory[i+1] and orders>=factor*(inventory[i]-inventory[i+1]):
                ans+=factor*getSum(inventory[i],inventory[i+1])
                orders-=factor*(inventory[i]-inventory[i+1])
            elif i==n-1 or inventory[i]>inventory[i+1]:
                sell_all=orders//factor
                ans+=factor*getSum(inventory[i],inventory[i]-sell_all)
                rem=orders%factor
                ans+=rem*(inventory[i]-sell_all)
                break
            i+=1
            factor+=1
        mod=10**9+7
        return ans%mod