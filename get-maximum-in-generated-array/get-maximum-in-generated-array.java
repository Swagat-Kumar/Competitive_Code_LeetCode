import java.util.*;
class Solution {
    public int getMaximumGenerated(int n) {
        if(n<=1){
            return n;
        }
        int[] dp=new int[n+1];
        dp[1]=1;
        for(int x=2;x<=n;x++){
            if(x%2==0){
                dp[x]=dp[x/2];
            }else{
                dp[x]=dp[x/2]+dp[x/2+1];
            }
        }
        int max=-1;
        for(int i=0;i<n+1;i++){
            max=Math.max(max,dp[i]);
        }
        return max;
    }
}