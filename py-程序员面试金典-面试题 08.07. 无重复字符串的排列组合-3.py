class Solution(object):
    """
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
输入：S = "qwe"
输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
输入：S = "ab"
输出：["ab", "ba"]
字符都是英文字母。字符串长度在[1, 9]之间。
链接：https://leetcode-cn.com/problems/permutation-i-lcci
    """
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def dfs(strings):
            if not strings:
                ret.append(''.join(rec))
                return
            for i, x in enumerate(strings):
                rec.append(x)
                dfs(strings[:i] + strings[i + 1:])
                rec.pop()

        ret, rec = [], []
        dfs(S)
        return ret


def main():
    S = "qwe"
    # S = "ab"
    test = Solution()
    ret = test.permutation(S)
    print(ret)


if __name__ == '__main__':
    main()
