//https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
Append value attribute to the list.
For each child of the root, recursively call the function till the root is None.
Return the list 
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        traversal_list = []
        if root is None:
            return []
        traversal_list.append(root.val)
        for i in root.children:
            traversal_list.extend(self.preorder(i))
        return traversal_list
