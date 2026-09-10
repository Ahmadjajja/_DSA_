class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for src, dst in connections:
            graph[src].append((dst, 1))
            graph[dst].append((src, 0))
            
        count = 0
        visit = set()
        def dfs(node):
            nonlocal count
            visit.add(node)
            for nei, dirCost in graph[node]:
                if nei in visit:
                    continue
                count += dirCost
                dfs(nei)		
            
        dfs(0)
        return count

        