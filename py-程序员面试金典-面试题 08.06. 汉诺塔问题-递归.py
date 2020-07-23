class Solution(object):
    """
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。
一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。
移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。
请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。
你需要原地修改栈。
输入：A = [2, 1, 0], B = [], C = []
输出：C = [2, 1, 0]
输入：A = [1, 0], B = [], C = []
输出：C = [1, 0]
A中盘子的数目不大于14个。
链接：https://leetcode-cn.com/problems/hanota-lcci
    """
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        def move(p1, p2, p3, n):
            if n == 1:
                p3.append(p1.pop())
            else:
                move(p1, p3, p2, n - 1)
                p3.append(p1.pop())
                move(p2, p1, p3, n - 1)

        move(A, B, C, len(A))
        return C


def main():
    A, B, C = [2, 1, 0], [], []
    A, B, C = [1, 0], [], []
    test = Solution()
    ret = test.hanota(A, B, C)
    print(ret)


if __name__ == '__main__':
    main()
