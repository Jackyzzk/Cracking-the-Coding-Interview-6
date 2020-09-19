# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。
实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，
转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
返回转换后的单向链表的头节点。
注意：本题相对原题稍作改动
输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
        4
    2       5
  1   3   N   6
0
提示：
节点数量不会超过 100000。
链接：https://leetcode-cn.com/problems/binode-lcci
    """
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        def dfs():  # 中序遍历
            que, p = [], root
            while que or p:
                while p:
                    que.append(p)
                    p = p.left
                p = que.pop()
                rec.append(p)
                p = p.right

        rec = []
        dfs()
        for i in range(len(rec) - 1):
            rec[i].left = None
            rec[i].right = rec[i + 1]
        rec[-1].left = rec[-1].right = None
        return rec[0]


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
    nums = [4, 2, 5, 1, 3, None, 6, 0]
    root = create(nums)
    test = Solution()
    ret = test.convertBiNode(root)
    print(ret)


if __name__ == '__main__':
    main()
