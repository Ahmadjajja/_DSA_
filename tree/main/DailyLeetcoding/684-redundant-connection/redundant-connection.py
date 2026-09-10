from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])  # path compression
            return par[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False  # already connected -> redundant edge

            # union by rank: attach shorter tree under taller tree
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                if rank[p1] == rank[p2]:
                    rank[p1] += 1
            else:
                par[p1] = p2

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]