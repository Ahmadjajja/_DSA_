class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        visit = set()
        def dfs(node, time):
            if len(adjList[node]) == 0:
                if hasApple[node]:
                    return [True, time]
                return [False, time]
            
            ans = False
            visit.add(node)
            for nei in adjList[node]:
                if nei in visit:
                    continue
                time += 1
                hasAp, t = dfs(nei, time)
                if hasAp:
                    t += 1
                else:
                    t -= 1
                time = t
                
                ans = ans or hasAp
            visit.remove(node)
            
            return [ans or hasApple[node], time]

        
        return dfs(0, 0)[1]
        
        