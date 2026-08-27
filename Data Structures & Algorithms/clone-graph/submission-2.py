"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        clone = {}

        def dfs(node: Node) -> Node:
            if node in clone:
                return clone[node]
            new_node = Node(node.val)
            clone[node] = new_node

            for neighbor in node.neighbors:
                new_node_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_node_neighbor)

            return new_node

        return dfs(node)