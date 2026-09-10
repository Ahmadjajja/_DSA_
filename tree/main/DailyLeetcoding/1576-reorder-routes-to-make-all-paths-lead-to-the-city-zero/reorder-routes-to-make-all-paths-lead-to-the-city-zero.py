class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for src, dst in connections:
            graph[src].append((dst, 1))
            graph[dst].append((src, 0))

        visit = set()
        def dfs(node, count):
            visit.add(node)
            count = 0
            for nei, dirCost in graph[node]:
                if nei not in visit:
                    count += dfs(nei, count) + dirCost
            	
            return count

        return dfs(0, 0)

        