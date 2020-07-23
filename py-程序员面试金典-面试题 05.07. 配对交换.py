class Solution(object):
    """
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令
（也就是说，位0与位1交换，位2与位3交换，以此类推）。
 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
 输入：num = 3
 输出：3
num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。
链接：https://leetcode-cn.com/problems/exchange-lcci
    """
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        odd = 0x55555555
        even = 0xaaaaaaaa
        a = num & odd
        b = num & even
        ret = (a << 1) | (b >> 1)
        return ret


def main():
    num = 3
    test = Solution()
    ret = test.exchangeBits(num)
    print(ret)


if __name__ == '__main__':
    main()
