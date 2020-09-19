class Solution(object):
    """
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]
输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
1 <= array1.length, array2.length <= 100000
链接：https://leetcode-cn.com/problems/sum-swap-lcci
    """
    def findSwapValues(self, array1, array2):
        """
        :type array1: List[int]
        :type array2: List[int]
        :rtype: List[int]
        """
        diff = sum(array2) - sum(array1)  # 假设 s2 > s1，diff > 0
        if diff & 1:
            return []
        diff >>= 1
        array1 = set(array1)
        for x in array2:
            if x - diff in array1:
                return [x - diff, x]
        return []


def main():
    array1, array2 = [4, 1, 2, 1, 1, 2], [3, 6, 3, 3]
    array1, array2 = [1, 2, 3], [4, 5, 6]
    test = Solution()
    ret = test.findSwapValues(array1, array2)
    print(ret)


if __name__ == '__main__':
    main()
