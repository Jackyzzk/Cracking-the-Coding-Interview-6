class Solution(object):
    """
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
输入: numbers = [1,2]
输出: [2,1]
numbers.length == 2
链接：https://leetcode-cn.com/problems/swap-numbers-lcci
    """
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        # numbers[0], numbers[1] = numbers[1], numbers[0]
        numbers[0] ^= numbers[1]
        numbers[1] ^= numbers[0]
        numbers[0] ^= numbers[1]
        return numbers


def main():
    nums = [1, 2]
    test = Solution()
    ret = test.swapNumbers(nums)
    print(ret)


if __name__ == '__main__':
    main()
