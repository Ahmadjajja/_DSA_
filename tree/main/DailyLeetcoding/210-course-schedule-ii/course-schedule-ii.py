# class Solution:
#     def findOrder(self, numCourses, prerequisites):
#         # build graph: course -> pre
#         adj = {i: [] for i in range(numCourses)}
#         for course, pre in prerequisites:
#             adj[course].append(pre)

#         visiting = set()   # current recursion stack
#         visited = set()    # fully processed
#         res = []           # topo order 

#         def dfs(node):
#             if node in visiting:
#                 return False        # found cycle
#             if node in visited:
#                 return True         # already done

#             visiting.add(node)

#             for nei in adj[node]:
#                 if not dfs(nei):
#                     return False

#             visiting.remove(node)
#             visited.add(node)
#             res.append(node)        # postorder

#             return True

#         for c in range(numCourses):
#             if c not in visited:
#                 if not dfs(c):
#                     return []       # cycle → no order

#         return res            # reverse to get correct order


from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 1) build graph: pre -> course
        adj = {i: [] for i in range(numCourses)}
        indeg = [0] * numCourses      # indegree[i] = how many prereqs i still needs

        for course, pre in prerequisites:
            adj[course].append(pre)
            indeg[pre] += 1

        # 2) start with all courses that have NO prereqs
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        res = []

        # 3) BFS
        while q:
            cur = q.popleft()
            res.append(cur)

            # "Take" this course ⇒ its dependents lose one prereq
            for nei in adj[cur]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        # 4) if we placed all courses, res is valid order; else there was a cycle
        if len(res) == numCourses:
            return res[::-1]
        return []
