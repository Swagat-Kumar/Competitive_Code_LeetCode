class Solution {
    public int maxProfit(int[] prices) {
        int firstBuy=-1000000;
        int firstSell=0;
        for(int p:prices){
            firstBuy=Math.max(firstBuy,-p);
            firstSell=Math.max(firstSell,p+firstBuy);
        }
        return firstSell;
    }
}