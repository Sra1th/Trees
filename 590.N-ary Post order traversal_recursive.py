//https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
For each child of the root, recursively call the function till the root is None.
Append the value of the root to the list
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

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        traversal_list = []
        for i in root.children:
            traversal_list.extend(self.postorder(i))
        traversal_list.append(root.val)
        return traversal_list