class Solution(object):
    """
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
输入：A = 1, B = 10  输出：10
输入：A = 3, B = 4   输出：12
保证乘法范围不会溢出
链接：https://leetcode-cn.com/problems/recursive-mulitply-lcci
    """
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        # a * b = a * 2 * b / 2
        if A < B:
            A, B = B, A
        if not B:
            return 0
        if B & 1:
            return A + self.multiply(A << 1, B >> 1)
        else:
            return self.multiply(A << 1, B >> 1)


def main():
    a, b = 1, 10
    # a, b = 3, 4
    test = Solution()
    ret = test.multiply(a, b)
    print(ret)


if __name__ == '__main__':
    main()
