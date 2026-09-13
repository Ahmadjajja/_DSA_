class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)
        def bfs(i):
            if odd[i]:
                return True
            odd[i] = -1
            q = deque([i])
            while q:
                index = q.popleft()
                for nei in graph[index]:
                    if odd[nei] == odd[index]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[index]
            return True


        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True