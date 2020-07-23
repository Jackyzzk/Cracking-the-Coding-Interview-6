class Solution(object):
    """
设计一个算法，算出 n 阶乘有多少个尾随零。
输入: 3   输出: 0   解释: 3! = 6, 尾数中没有零。
输入: 5   输出: 1   解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
链接：https://leetcode-cn.com/problems/factorial-zeros-lcci
    """
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count


def main():
    n = 25
    test = Solution()
    ret = test.trailingZeroes(n)
    print(ret)


if __name__ == '__main__':
    main()
