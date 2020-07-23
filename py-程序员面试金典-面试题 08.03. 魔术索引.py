class Solution(object):
    """
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，
如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
输入：nums = [0, 2, 3, 4, 5]
输出：0
说明: 0下标的元素为0
输入：nums = [1, 1, 1]
输出：1
nums长度在[1, 1000000]之间
链接：https://leetcode-cn.com/problems/magic-index-lcci
    """
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, x in enumerate(nums):
            if x == i:
                return x
        return -1


def main():
    nums = [0, 2, 3, 4, 5]
    # nums = [1, 1, 1]
    # nums = [0, 0, 2]  # 0
    test = Solution()
    ret = test.findMagicIndex(nums)
    print(ret)


if __name__ == '__main__':
    main()
