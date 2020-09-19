class Solution(object):
    """
珠玑妙算游戏（the game of master mind）的玩法如下。
计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。
例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。
打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；
要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。
给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，
其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。

输入： solution="RGBY",guess="GGRR"
输出： [1,1]
解释： 猜中1次，伪猜中1次。
len(solution) = len(guess) = 4
solution和guess仅包含"R","G","B","Y"这4种字符
链接：https://leetcode-cn.com/problems/master-mind-lcci
    """
    def masterMind(self, solution, guess):
        """
        :type solution: str
        :type guess: str
        :rtype: List[int]
        """
        guess_dict = {}
        rec1, rec2 = 0, 0

        for x in guess:
            guess_dict[x] = guess_dict.get(x, 0) + 1

        for i, x in enumerate(solution):
            if x == guess[i]:
                rec1 += 1
            # if x in guess_dict and guess_dict[x] > 0:
            if guess_dict.get(x, 0) > 0:
                guess_dict[x] -= 1
                rec2 += 1

        return [rec1, rec2 - rec1]


def main():
    solution, guess = "RGBY", "GGRR"
    # solution, guess = "BGBG", "RGBR"  # 2, 0
    test = Solution()
    ret = test.masterMind(solution, guess)
    print(ret)


if __name__ == '__main__':
    main()
