class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UF:
            def __init__(self,v):
                self.id=[i for i in range(v)]
                self.sz=[0 for i in range(v)]
                self.c=v
            def root(self,x):
                while x!=self.id[x]:
                    self.id[x]=self.id[self.id[x]]
                    x=self.id[x]
                return x
            def count(self):
                return self.c
            def union(self,x,y):
                i=self.root(x)
                j=self.root(y)
                if i==j:
                    return
                if self.sz[i]<self.sz[j]:
                    self.id[i]=j
                elif self.sz[i]>self.sz[j]:
                    self.id[j]=i
                else:
                    self.sz[i]+=1
                    self.id[j]=i
                self.c-=1
        n=len(isConnected)
        conn=UF(n)
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    conn.union(r,c)
        return conn.count()
                