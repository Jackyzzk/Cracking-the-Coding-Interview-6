class Solution(object):
    """
给定一个整数数组，找出总和最大的连续数列，并返回总和。
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
链接：https://leetcode-cn.com/problems/contiguous-sequence-lcci
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        rec_max, cur = float('-inf'), float('-inf')
        for i in range(n):
            cur = max(nums[i], cur + nums[i])
            rec_max = max(rec_max, cur)
        return rec_max


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [-1]
    test = Solution()
    ret = test.maxSubArray(nums)
    print(ret)


if __name__ == '__main__':
    main()
