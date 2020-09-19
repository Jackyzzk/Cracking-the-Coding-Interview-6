class Solution(object):
    """
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，
编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
输入: n = 5  输出：2
解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
输入: n = 10  输出：4
解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
你可以假设：0 <= n (总金额) <= 1000000
链接：https://leetcode-cn.com/problems/coin-lcci
    """
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = [1, 5, 10, 25]
        opt = [0] * (n + 1)
        opt[0] = 1
        for x in coins:
            for i in range(x, n + 1):
                opt[i] = (opt[i] + opt[i - x]) % 1000000007
        return opt[-1]


def main():
    n = 5
    n = 10
    n = 25  # 13
    test = Solution()
    ret = test.waysToChange(n)
    print(ret)


if __name__ == '__main__':
    main()
