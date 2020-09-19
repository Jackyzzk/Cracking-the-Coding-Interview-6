class Solution(object):
    """
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
说明：解集不能包含重复的子集。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
链接：https://leetcode-cn.com/problems/bracket-lcci
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right):
            if left == right == n:
                ret.append(''.join(rec))
                return
            if left < n:
                rec.append('(')
                dfs(left + 1, right)
                rec.pop()
            if right < left:
                rec.append(')')
                dfs(left, right + 1)
                rec.pop()

        ret, rec = [], []
        dfs(0, 0)
        return ret


def main():
    n = 4
    test = Solution()
    ret = test.generateParenthesis(n)
    print(ret)


if __name__ == '__main__':
    main()
