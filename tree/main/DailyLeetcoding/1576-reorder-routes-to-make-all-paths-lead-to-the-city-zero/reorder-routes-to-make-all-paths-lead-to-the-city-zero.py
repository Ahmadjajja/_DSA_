class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        outward = {i: [] for i in range(n)}
        inward = {i: [] for i in range(n)}

        for src, dst in connections:
            outward[src].append(dst)
            inward[dst].append(src)
        count = 0
        visit = set()
        def dfs(node):
            nonlocal count
            visit.add(node)
            for nei in outward[node]:
                if nei in visit:
                    continue
                dfs(nei)
                count += 1
            for nei in inward[node]:
                if nei in visit:
                    continue	
                dfs(nei)		
            
        dfs(0)
        return count

        