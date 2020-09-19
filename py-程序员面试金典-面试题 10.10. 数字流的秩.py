class StreamRank(object):
    """
假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。
请实现数据结构和算法来支持这些操作，也就是说：
实现 track(int x) 方法，每读入一个数字都会调用该方法；
实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。
输入:
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
输出:
[null,0,null,1]
提示：x <= 50000
track 和 getRankOfNumber 方法的调用次数均不超过 2000 次
链接：https://leetcode-cn.com/problems/rank-from-stream-lcci
    """
    def __init__(self):
        self.que = []

    def track(self, x):
        """
        :type x: int
        :rtype: None
        """


    def getRankOfNumber(self, x):
        """
        :type x: int
        :rtype: int
        """


def main():
    commands = ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"], [[], [1], [0], [0]]
    test = StreamRank()
    ret = [None]
    for i, x in enumerate(commands[0]):
        if x == 'getRankOfNumber':
            ret.append(test.getRankOfNumber(commands[1][i][0]))
        elif x == 'track':
            ret.append(None)
    print(ret)


if __name__ == '__main__':
    main()



# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)