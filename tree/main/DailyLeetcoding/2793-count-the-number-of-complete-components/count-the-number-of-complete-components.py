class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, res):
            if node in visited:
                return res
            visited.add(node)
            res.append(node)
            for nei in adjList[node]:
                dfs(nei, res)
            return res

        ans = 0
        for i in range(n):
            if i in visited:
                continue
            component = dfs(i, [])
            flag = True
            for node in component:
                if len(component) - 1 != len(adjList[node]):
                    flag = False
                    break
            
            if flag:
                ans += 1

        return ans
