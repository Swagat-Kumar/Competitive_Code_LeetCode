class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph={}
        for t in tickets:
            if t[0] not in graph:
                graph[t[0]]=[t[1]]
            else:
                graph[t[0]].append(t[1])
        for g in graph:
            graph[g].sort()
        print(graph)
        ans=[]
        st=[]
        def dfs(source='JFK'):
            st.append(source)
            if source not in graph or len(graph[source])==0:
                ans.append(st.pop())
                return
            while len(graph[source])!=0:
                v=graph[source].pop(0)
                dfs(v)
            ans.append(st.pop())
        dfs()
        return ans[::-1]
            
            