import heapq
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==0:
            return []
        if n==1:
            return [0]
        graph=[[] for i in range(n)]
        count=[0]*n
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            count[e[0]]+=1
            count[e[1]]+=1
        q=[]
        for i in range(n):
            if count[i]==1:
                q.append(i)
        x=n
        while x>2:
            size=len(q)
            x=x-size
            while size>0:
                v=q.pop(0)
                for a in graph[v]:
                    count[a]-=1
                    if count[a]==1:
                        q.append(a)
                size-=1
        return q