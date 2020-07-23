class Solution(object):
    """
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。
你有办法在O(n)时间内完成吗？
输入：[3,0,1]               输出：2
输入：[9,6,4,2,3,5,7,0,1]   输出：8
链接：https://leetcode-cn.com/problems/missing-number-lcci
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, n = 0, len(nums)
        for i in range(n):
            ret ^= i ^ nums[i]
        ret ^= n
        return ret


def main():
    nums = [3, 0, 1]
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    test = Solution()
    ret = test.missingNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
