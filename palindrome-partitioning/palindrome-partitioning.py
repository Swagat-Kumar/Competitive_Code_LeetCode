class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def solve(aux=[],i=0):
            if i>=len(s):
                for a in aux:
                    if a!=a[::-1]:
                        return
                ans.append(list(aux))
                return
            temp=list(aux)
            temp.append(s[i])
            solve(temp,i+1)
            temp=list(aux)
            if len(temp)!=0:
                temp[-1]+=s[i]
                solve(temp,i+1)
        solve()
        return ans
            
                
                    
                