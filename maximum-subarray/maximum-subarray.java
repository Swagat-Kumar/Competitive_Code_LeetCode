class Solution {
    public int maxSubArray(int[] nums) {
        int aux=0;
        int ans=nums[0];
        for(int i=0;i<nums.length;i++){
            aux+=nums[i];
            ans=Math.max(ans,aux);
            if(aux<0){
                aux=0;
            }
        }
        return ans;
    }
}