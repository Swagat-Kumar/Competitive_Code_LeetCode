class Solution {
    public boolean isSubsequence(String s, String t) {
        int ls=s.length();
        int lt=t.length();
        boolean[][] dp=new boolean[ls+1][lt+1];
        for(int r=0;r<ls+1;r++){
            for(int c=0;c<lt+1;c++){
                if(r==0){
                    dp[r][c]=true;
                }else if(c==0){
                    dp[r][c]=false;
                }else if(s.charAt(r-1)==t.charAt(c-1)){
                    dp[r][c]=dp[r-1][c-1];
                }else{
                    dp[r][c]=dp[r][c-1];
                }
            }
        }
        return dp[ls][lt];
    }
}