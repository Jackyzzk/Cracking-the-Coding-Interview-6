class Solution(object):
    """
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
输出：-1
说明: 不存在返回-1。
输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
输出：4
words的长度在[1, 1000000]之间
链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
    """
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        for i, x in enumerate(words):
            if x == s:
                return i
        return -1


def main():
    words, s = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], "ta"
    # words, s = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], "ball"
    test = Solution()
    ret = test.findString(words, s)
    print(ret)


if __name__ == '__main__':
    main()
