class Solution(object):
    """
插入。给定两个32位的整数N与M，以及表示比特位置的i与j。
编写一种方法，将M插入N，使得M从N的第j位开始，到第i位结束。
假定从j位到i位足以容纳M，也即若M = 10 011，那么j和i之间至少可容纳5个位。
例如，不可能出现j = 3和i = 2的情况，因为第3位和第2位之间放不下M。
输入：N = 10000000000, M = 10011, i = 2, j = 6
输出：N = 10001001100
输入： N = 0, M = 11111, i = 0, j = 4
输出：N = 11111
链接：https://leetcode-cn.com/problems/insert-into-bits-lcci
    """
    def insertBits(self, N, M, i, j):
        """
        :type N: int
        :type M: int
        :type i: int
        :type j: int
        :rtype: int
        """
        for k in range(j - i + 1):
            N &= ~(1 << (i + k))  # 把 N 的第 i + k 位变为 0，相当于掩码 11111101111
        N |= M << i
        return N


def main():
    N, M, i, j = 0b10000000000, 0b10011, 2, 6
    # N, M, i, j = 0, 11111, 0, 4
    test = Solution()
    ret = test.insertBits(N, M, i, j)
    print(bin(ret))


if __name__ == '__main__':
    main()
