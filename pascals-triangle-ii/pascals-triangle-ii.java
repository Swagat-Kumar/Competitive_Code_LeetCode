class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ans= new ArrayList<Integer>();
        ans.add(1);
        for(int i=0;i<rowIndex;i++){
            List<Integer> aux=new ArrayList<Integer>();
            aux.add(1);
            for(int x=0;x<i;x++){
                aux.add(ans.get(x)+ans.get(x+1));
            }
            aux.add(1);
            ans=aux;
            
        }
        return ans;
    }
}