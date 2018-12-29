//https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
Push the root to stack
While Stack is not empty
	Pop the stack and store it in a root variable
	Append the value attribute of the root variable into a list
	Extend the stack by appending the children of the root variable
Return the list in reversed order.
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
        stack = [root]
        while stack:
            cur_node = stack.pop()
            traversal_list.append(cur_node.val)
            stack.extend(cur_node.children)
        return traversal_list[::-1]
