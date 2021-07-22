class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for i in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])
        state=[0]*numCourses
        postOrder=[]
        def dfs(v):
            if state[v]==1:
                return False
            if state[v]==2:
                return True
            state[v]=1
            for i in graph[v]:
                if not dfs(i):
                    return False
            postOrder.append(v)
            state[v]=2
            return True
        for v in range(numCourses):
            if not dfs(v):
                return []
        return postOrder