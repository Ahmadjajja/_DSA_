class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        time = 0
        visit = set()
        def dfs(node):
            nonlocal time
            if len(adjList[node]) == 0:
                if hasApple[node]:
                    return True
                return False
            
            ans = False
            visit.add(node)
            for nei in adjList[node]:
                if nei in visit:
                    continue
                time += 1
                hasAp = dfs(nei)
                if hasAp:
                    time += 1
                else:
                    time -= 1
                
                ans = ans or hasAp
            visit.remove(node)
            
            return ans or hasApple[node]

        dfs(0)
        return time
        
        