class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UF:
            def __init__(self):
                self.id=[i for i in range(1001)]
                self.sz=[0 for i in range(1001)]
            def root(self,x):
                while x!=self.id[x]:
                    self.id[x]=self.id[self.id[x]]
                    x=self.id[x]
                return x
            def union(self,x,y):
                i=self.root(x)
                j=self.root(y)
                if i==j:
                    return True
                if self.sz[i]<self.sz[j]:
                    self.id[i]=j
                elif self.sz[i]>self.sz[j]:
                    self.id[j]=i
                else:
                    self.id[j]=i
                    self.sz[i]+=1
                return False
        aux=UF()
        for e in edges:
            if aux.union(e[0],e[1]):
                return e
        