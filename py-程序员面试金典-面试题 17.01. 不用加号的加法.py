class Solution(object):
    """
设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。
输入: a = 1, b = 1
输出: 2
a, b 均可能是负数或 0
结果不会溢出 32 位整数
链接：https://leetcode-cn.com/problems/add-without-plus-lcci
    """
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a &= 0xffffffff
        b &= 0xffffffff

        # carry = (a & b) << 1
        # basic = a ^ b
        while b:
            a, b = a ^ b, ((a & b) << 1) & 0xffffffff
        return a if a < 0x80000000 else ~(a ^ 0xffffffff)


def main():
    a, b = 1, -3
    test = Solution()
    ret = test.add(a, b)
    print(ret)


if __name__ == '__main__':
    main()
