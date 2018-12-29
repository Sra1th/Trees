// https: // leetcode.com / problems / n - ary - tree - preorder - traversal /

"""
Push the root to stack
While Stack is not empty
	Pop the stack and store it in a root variable
	Append the value attribute of the root variable into a list
	Extend the stack by appending the children of the root variable in reversed order (considering from first left subtree in resultant list).
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
        if root is None:
            return []
        stack = [root]
        traversal_list = []
        while stack:
            cur_root = stack.pop()
            traversal_list.append(cur_root.val)
            stack.extend(reversed(cur_root.children))
        return traversal_list
