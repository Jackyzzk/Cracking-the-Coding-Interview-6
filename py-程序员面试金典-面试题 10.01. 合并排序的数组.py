class Solution(object):
    """
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。
编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
A.length == n + m
链接：https://leetcode-cn.com/problems/sorted-merge-lcci
    """
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        p1, p2, i = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if A[p1] > B[p2]:
                A[i] = A[p1]
                p1 -= 1
            else:
                A[i] = B[p2]
                p2 -= 1
            i -= 1
        while p2 >= 0:
            A[i] = B[p2]
            p2 -= 1
            i -= 1
        return A


def main():
    A, m = [1, 2, 3, 0, 0, 0], 3
    B, n = [2, 5, 6], 3
    # A, m = [0], 0
    # B, n = [1], 1
    test = Solution()
    ret = test.merge(A, m, B, n)
    print(ret)


if __name__ == '__main__':
    main()
