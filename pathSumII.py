'''
Prompt:
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''
from treeNode import TreeNode

def pathSum(root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: List[List[int]]
    """
    
    cur = root
    sumNodes = 0
    visNodes = [] # stack containing [cur,cur.val]
    ans = []
    if root == None:
        return ans
    if root.val == targetSum and root.right == None and root.left == None:
        return [[root.val]]
    def dfs(sumNodes, visNodes, ans, cur):
        enmStatus = 0

        if sumNodes == targetSum and visNodes and visNodes[-1][0].left == None and visNodes[-1][0].right == None:

            ans.append([row[1] for row in visNodes])
            return 1 #skip right
        
        if cur!= None:
            sumNodes+= cur.val
            visNodes.append([cur,cur.val])
            enmstatus =  dfs(sumNodes, visNodes, ans, cur.left)
            if enmstatus != 1:
                dfs(sumNodes, visNodes, ans, cur.right)
        if visNodes and cur == visNodes[-1][0]:
            tmp = visNodes.pop(-1)
            cur = tmp[0]
            sumNodes-=tmp[1]
        return 0# continue

    dfs(sumNodes, visNodes, ans, cur)
    return ans

if __name__ == "__main__":
    root = TreeNode(5,TreeNode(4,None,None), TreeNode(8,None,None))
    four = root.left
    eight = root.right
    four.left = TreeNode(11,TreeNode(7,None,None),TreeNode(2,None,None))
    eight.left = TreeNode(13,None,None)
    eight.right = TreeNode(4,TreeNode(5,None,None),TreeNode(1,None,None))
    print(pathSum(root,22))