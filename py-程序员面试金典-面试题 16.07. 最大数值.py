class Solution(object):
    """
编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
输入： a = 1, b = 2
输出： 2
链接：https://leetcode-cn.com/problems/maximum-lcci
    """
    def maximum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        sign = ((a - b) & 0x1ffffffff) >> 32
        # if sign == 1: a < b
        # if sign == 0: a > b
        return a * (sign ^ 1) + b * (sign ^ 0)


def main():
    a, b = 3, 2
    # a, b = 2147483647, -2147483648
    test = Solution()
    ret = test.maximum(a, b)
    print(ret)


if __name__ == '__main__':
    main()
