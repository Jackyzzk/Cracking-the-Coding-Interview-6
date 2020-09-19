# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
实现一个函数，检查二叉树是否平衡。在这个问题中，
平衡树的定义如下：任意一个节点，其两棵子树的高度0。
给定二叉树 [3,9,20,None,None,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
给定二叉树 [1,2,2,3,3,None,None,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。
链接：https://leetcode-cn.com/problems/check-balance-lcci
    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1


def create(nums):
    if not nums:
        return None
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = TreeNode(left) if left is not None else None
        node.right = TreeNode(right) if right is not None else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return root


def main():
    nums = [3, 9, 20, None, None, 15, 7]
    # nums = [1, 2, 2, 3, 3, None, None, 4, 4]
    # nums = [1,2,2,3,None,None,3,4,None,None,4]  # false
    test = Solution()
    root = create(nums)
    ret = test.isBalanced(root)
    print(ret)


if __name__ == '__main__':
    main()
