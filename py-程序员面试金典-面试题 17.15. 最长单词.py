class Solution(object):
    """
给定一组单词words，编写一个程序，找出其中的最长单词，
且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，
返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。
输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
输出： "dogwalker"
解释： "dogwalker"可由"dog"和"walker"组成。
0 <= len(words) <= 100
1 <= len(words[i]) <= 100
链接：https://leetcode-cn.com/problems/longest-word-lcci
    """
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words_set = set(words)
        n = len(words)
        opt = [[0] for i in range(n)]
        ret = []
        for i, x in enumerate(words):
            length = len(x)
            for p2 in range(length):
                for p1 in opt[i]:
                    if x[p1:p2 + 1] in words_set:
                        opt[i][0:0] = [p2]
                        break
            if opt[i][0] == length - 1 and len(opt[i]) > 2:
                ret.append((length, i))

        ret.sort(key=lambda x: (-x[0], x[1]))
        return words[ret[0][1]] if ret else ''


def main():
    words = ["cat","banana","dog","nana","walk","walker","dogwalker"]
    test = Solution()
    ret = test.longestWord(words)
    print(ret)


if __name__ == '__main__':
    main()
