class Solution(object):
    """
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
输入: num = 1775(11011101111)
输出: 8
输入: num = 7(0111)
输出: 4
链接：https://leetcode-cn.com/problems/reverse-bits-lcci
    """
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        rec = -1  # 记录第一个 0 的位置
        ret = 0
        p1, p2 = -1, -1  # 滑动窗口
        while num:
            if num & 1:
                num >>= 1
                p1 += 1
            elif p2 == rec:
                num >>= 1
                p1 += 1
                rec = p1
            else:
                ret = max(ret, p1 - p2)
                p2 = rec
                num >>= 1
                p1 += 1
                rec = p1
        if p2 == rec:
            p1 += 1
        ret = max(ret, p1 - p2)
        return ret


def main():
    num = 0b11011101111
    num = 0b0111
    test = Solution()
    ret = test.reverseBits(num)
    print(ret)


if __name__ == '__main__':
    main()
