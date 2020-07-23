class Solution(object):
    """
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
输入：[1,2,5,9,5,9,5,5,5]
输出：5
输入：[3,2]
输出：-1
输入：[2,2,1,1,1,2,2]
输出：2
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？
链接：https://leetcode-cn.com/problems/find-majority-element-lcci
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 摩尔投票
        n = len(nums)
        if not n:
            return -1
        count, p = 1, nums[0]
        for i in range(1, n):
            if count > 0:
                if nums[i] == p:
                    count += 1
                else:
                    count -= 1
            else:
                p = nums[i]
                count = 1
        return p if count else -1


def main():
    nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    # nums = [3, 2]
    # nums = [2, 2, 1, 1, 1, 2, 2]
    test = Solution()
    ret = test.majorityElement(nums)
    print(ret)


if __name__ == '__main__':
    main()
