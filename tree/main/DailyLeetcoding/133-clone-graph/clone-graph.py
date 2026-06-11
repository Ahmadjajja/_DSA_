"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        clone = {}

        def dfs(cur):

            copy = Node()
            copy.val = cur.val
            clone[cur] = copy

            for nei in cur.neighbors:
                if nei not in clone:
                    dfs(nei)
                copy.neighbors.append(clone[nei])
            
            return copy

        return dfs(node)