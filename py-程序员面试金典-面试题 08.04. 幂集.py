class Solution(object):
    """
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。
说明：解集不能包含重复的子集。
输入： nums = [1,2,3]
输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
链接：https://leetcode-cn.com/problems/power-set-lcci
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start):
            for i in range(start, n):  # 组合用不回头的 for 循环就不用标记 visited 记录了
                rec.append(nums[i])
                ret.append(rec[:])
                dfs(i + 1)
                rec.pop()

        rec, ret = [], [[]]
        n = len(nums)
        dfs(0)
        return ret


def main():
    nums = [1, 2, 3]
    test = Solution()
    ret = test.subsets(nums)
    print(ret)


if __name__ == '__main__':
    main()
