class Solution(object):
    """
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
输入: "3+2*2"       输出: 7
输入: " 3/2 "       输出: 1
输入: " 3+5 / 2 "   输出: 5
你可以假设所给定的表达式都是有效的。请不要使用内置的库函数 eval。
链接：https://leetcode-cn.com/problems/calculator-lcci
    """
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = {'+', '-', '*', '/'}


def main():
    math = "3+2*2"
    math = " 3/2 "
    math = " 3+5 / 2 "
    test = Solution()
    ret = test.calculate(math)
    print(ret)


if __name__ == '__main__':
    main()
