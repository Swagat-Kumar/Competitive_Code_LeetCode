class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[1]
        for i in range(rowIndex):
            aux=[1]
            for i in range(len(ans)-1):
                aux.append(ans[i]+ans[i+1])
            aux.append(1)
            ans=aux
        return ans
                