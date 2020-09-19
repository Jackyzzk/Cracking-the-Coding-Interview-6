class Solution(object):
    """
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
输入：S = "qqe"
输出：["eqq","qeq","qqe"]
输入：S = "ab"
输出：["ab", "ba"]
字符都是英文字母。字符串长度在[1, 9]之间。
链接：https://leetcode-cn.com/problems/permutation-ii-lcci
    """
    def permutation(self, S):
        # permutation n.排列(方式); 组合(方式); 置换;
        """
        :type S: str
        :rtype: List[str]
        """
        s = list(S)
        s.sort()

        def dfs():
            if len(rec) == n:
                ret.append(''.join(rec))
                return
            for i, x in enumerate(s):
                if not self.visited >> i & 1:
                    if i and x == s[i - 1] and not self.visited >> (i - 1) & 1:
                        continue
                    self.visited |= 1 << i
                    rec.append(x)
                    dfs()
                    rec.pop()
                    self.visited ^= 1 << i

        rec, ret,  n = [], [], len(s)
        self.visited = 0
        dfs()
        return ret


def main():
    s = "qqe"
    s = "ab"
    s = "www"
    test = Solution()
    ret = test.permutation(s)
    print(ret)


if __name__ == '__main__':
    main()
