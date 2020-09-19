class Solution(object):
    """
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
    """
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        select = ignore = 0
        for x in nums:
            select, ignore = x + ignore, max(select, ignore)
        return max(select, ignore)


def main():
    nums = [1, 2, 3, 1]
    nums = [2, 7, 9, 3, 1]
    nums = [2, 1, 4, 5, 3, 1, 1, 3]
    test = Solution()
    ret = test.massage(nums)
    print(ret)


if __name__ == '__main__':
    main()
