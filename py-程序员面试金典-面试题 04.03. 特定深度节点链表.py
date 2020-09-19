# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表
（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。
输入：[1,2,3,4,5,null,7,8]
        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8
输出：[[1],[2,3],[4,5,7],[8]]
链接：https://leetcode-cn.com/problems/list-of-depth-lcci/
    """
    def listOfDepth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        def rebuild(nums):
            aux = p = ListNode(-1)
            for x in nums:
                p.next = ListNode(x)
                p = p.next
            return aux.next

        def bfs():
            que, aux, rec = [tree], [], []
            while que:
                p = que.pop(0)
                rec.append(p.val)
                if p.left:
                    aux.append(p.left)
                if p.right:
                    aux.append(p.right)
                if not que:
                    que, aux = aux, []
                    ret.append(rebuild(rec))
                    rec = []

        ret = []
        bfs()
        return ret


def create(nums):  # 15行代码
    if not nums:
        return None
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        p = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        p.left = TreeNode(left) if left is not None else None
        p.right = TreeNode(right) if right is not None else None
        if p.left:
            que.append(p.left)
        if p.right:
            que.append(p.right)
    return root


def main():
    nums = [1, 2, 3, 4, 5, None, 7, 8]
    root = create(nums)
    test = Solution()
    ret = test.listOfDepth(root)
    print(ret)


if __name__ == '__main__':
    main()
