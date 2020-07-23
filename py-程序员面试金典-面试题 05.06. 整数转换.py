class Solution(object):
    """
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。
输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
输出：2
输入：A = 1，B = 2
输出：2
A，B范围在[-2147483648, 2147483647]之间
链接：https://leetcode-cn.com/problems/convert-integer-lcci
    """
    def convertInteger(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        A &= 0xffffffff
        B &= 0xffffffff

        # 真值	  原码	       反码	        补码	   备注
        # + 1	0 00000001	0 00000001	0 00000001	正数的原码反码补码相同
        # - 1	1 00000001	1 11111110	1 11111111	负数的补码是符号位不变其余取反加 1

        # & 0xffffffff 相当于把符号位也考虑到后面的异或运算中来，直接异或是不考虑符号位的？

        aux = A ^ B
        count = 0
        while aux:
            if aux & 1:
                count += 1
            aux >>= 1
        return count


def main():
    A, B = 29, 15
    A, B = 1, -1
    # A, B = 826966453, -729934991
    test = Solution()
    ret = test.convertInteger(A, B)
    print(ret)


if __name__ == '__main__':
    main()
