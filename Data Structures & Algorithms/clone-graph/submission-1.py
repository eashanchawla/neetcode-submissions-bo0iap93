"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        newNode = Node(node.val)
        self.visited[node] = newNode
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                newNode.neighbors.append(self.visited[neighbor])
            else:
                newNode.neighbors.append(self.cloneGraph(neighbor))
        return newNode

