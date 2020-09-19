import random


class Solution(object):
    """
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))
链接：https://leetcode-cn.com/problems/smallest-k-lcci
    """
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr:
            return []

        def partition(left, right):
            mid, p2 = random.randint(left, right), left
            arr[mid], arr[p2] = arr[p2], arr[mid]
            for p1 in range(left + 1, right + 1):
                if arr[p1] < arr[left]:
                    p2 += 1
                    arr[p1], arr[p2] = arr[p2], arr[p1]
            arr[left], arr[p2] = arr[p2], arr[left]
            if p2 > k:
                partition(left, p2 - 1)
            if p2 < k:
                partition(p2 + 1, right)

        partition(0, len(arr) - 1)
        return arr[:k]


def main():
    arr, k = [1, 3, 5, 7, 2, 4, 6, 8], 4
    arr, k = [], 0
    test = Solution()
    ret = test.smallestK(arr, k)
    print(ret)


if __name__ == '__main__':
    main()
