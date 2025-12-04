class Solution:
    def findOrder(self, numCourses, prerequisites):
        # build graph: course -> pre
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        visiting = set()   # current recursion stack
        visited = set()    # fully processed
        res = []           # topo order 

        def dfs(node):
            if node in visiting:
                return False        # found cycle
            if node in visited:
                return True         # already done

            visiting.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            res.append(node)        # postorder

            return True

        for c in range(numCourses):
            if c not in visited:
                if not dfs(c):
                    return []       # cycle → no order

        return res            # reverse to get correct order
