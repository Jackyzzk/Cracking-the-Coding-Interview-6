# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
          0
         / \
       -3   9
       /   /
     -10  5
链接：https://leetcode-cn.com/problems/minimum-height-tree-lcci
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def rebuild(start, end):
            if start > end:
                return None
            mid = (start + end) >> 1
            root = TreeNode(nums[mid])
            root.left = rebuild(start, mid - 1)
            root.right = rebuild(mid + 1, end)
            return root

        return rebuild(0, len(nums) - 1)


def main():
    nums = [-10, -3, 0, 5, 9]
    test = Solution()
    ret = test.sortedArrayToBST(nums)
    print(ret)


if __name__ == '__main__':
    main()
