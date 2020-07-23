class Solution(object):
    """
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
输入：n = 3   输出：4  说明: 有四种走法
输入：n = 5   输出：13
n范围在[1, 1000000]之间
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
    """
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre2, pre1, cur = 0, 0, 1
        for i in range(n):
            pre2, pre1, cur = pre1, cur, (pre2 + pre1 + cur) % 1000000007
        return cur


def main():
    n = 5
    n = 90075
    test = Solution()
    ret = test.waysToStep(n)
    print(ret)


if __name__ == '__main__':
    main()
