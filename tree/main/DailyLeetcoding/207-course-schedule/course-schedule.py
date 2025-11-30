class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            adjList[pre[0]].append(pre[1])

        visit = set()

        def dfs(course):
            if len(adjList[course]) == 0:
                return True
            
            if course in visit:
                return False
                
            visit.add(course)
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            adjList[course] = []
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True