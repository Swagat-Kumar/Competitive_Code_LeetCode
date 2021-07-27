class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic={}
        for c in p:
            if c not in dic:
                dic[c]=1
            else:
                dic[c]+=1
        ans=[]
        if len(s)<len(p):
            return []
        aux={}
        for a in s[:len(p)]:
            if a not in aux:
                aux[a]=1
            else:
                aux[a]+=1
        if aux==dic:
            ans.append(0)
        for i in range(1,len(s)-len(p)+1):
            curr=s[i+len(p)-1]
            prev=s[i-1]
            
            if curr not in aux:
                aux[curr]=1
            else:
                aux[curr]+=1
            if aux[prev]==1:
                del aux[prev]
            else:
                aux[prev]-=1
            print(aux)
            if aux==dic:
                ans.append(i)
        return ans