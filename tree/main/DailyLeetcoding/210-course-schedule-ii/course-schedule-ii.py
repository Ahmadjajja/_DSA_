class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visiting = set() # current recursion stack
        visited = set() # fully processed
        res = []
        
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if crs in res:
                continue
            
            if not dfs(crs):
                return []
        print("crs -> ", crs)
        return res
        