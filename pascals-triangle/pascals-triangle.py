class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(numRows-1):
            aux=[1]
            for i in range(len(ans[-1])-1):
                aux.append(ans[-1][i]+ans[-1][i+1])
            aux.append(1)
            ans.append(aux)
        return ans
            
            