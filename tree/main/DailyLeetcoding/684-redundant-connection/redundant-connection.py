from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        size = [0] * (n + 1)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])  # path compression
            return par[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False  # already connected -> redundant edge

            # union by size: attach smaller tree under larger tree
            if size[p1] < size[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            size[p1] += size[p2]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        # Time Complexity:  O(n * α(n)) ~ O(n)
        #   - n union/find operations, each amortized O(α(n))
        #     (α = inverse Ackermann function, grows so slowly it's
        #     effectively constant, ≤ 4 for any realistic n)
        #   - achieved via path compression (flattens trees during find)
        #     + union by rank (keeps trees balanced during union)
        #
        # Space Complexity: O(n)
        #   - par array: O(n)
        #   - rank array: O(n)
        #   - find() recursion stack: O(log n) worst case pre-compression,
        #     O(1) amortized after compression flattens the tree