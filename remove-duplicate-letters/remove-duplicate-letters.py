class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        aux={}
        ans=[]
        visited=[False]*26
        for i in range(len(s)):
            aux[s[i]]=i
        for i in range(len(s)):
            if visited[ord(s[i])-97]:
                continue
            visited[ord(s[i])-97]=True
            while len(ans)>0 and ans[-1]>s[i] and aux[ans[-1]]>i:
                visited[ord(ans[-1])-97]=False
                ans.pop()
            ans.append(s[i])
        return ''.join(ans)            