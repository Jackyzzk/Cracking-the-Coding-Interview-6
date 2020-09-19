class TripleInOne(object):
    """
三合一。描述如何只用一个数组来实现三个栈。
你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、
peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
构造函数会传入一个stackSize参数，代表每个栈的大小。
输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
输出：
[null, null, null, null, 2, 1, -1, -1]
链接：https://leetcode-cn.com/problems/three-in-one-lcci
    """
    def __init__(self, stackSize):
        """
        :type stackSize: int
        """
        self.que = [3, 3 + stackSize, 3 + 2 * stackSize, stackSize] + [-1] * stackSize * 3
        self.length = stackSize

    def push(self, stackNum, value):
        """
        :type stackNum: int
        :type value: int
        :rtype: None
        """
        i = self.que[stackNum]  # 找到栈顶坐标
        if i + 1 < 4 + self.length * (stackNum + 1):
            self.que[i + 1] = value
            self.que[stackNum] += 1

    def pop(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        i = self.que[stackNum]
        if i >= 4 + self.length * stackNum:
            ret = self.que[i]
            self.que[i] = -1
            self.que[stackNum] -= 1
            return ret
        return -1

    def peek(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        i = self.que[stackNum]
        if i >= 4 + self.length * stackNum:
            return self.que[i]
        return -1

    def isEmpty(self, stackNum):
        """
        :type stackNum: int
        :rtype: bool
        """
        i = self.que[stackNum]
        if i >= 4 + self.length * stackNum:
            return False
        return True


def main():
    command1 = (["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"],
                [[1], [0, 1], [0, 2], [0], [0], [0], [0]])
    command2 = (["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"],
                [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]])
    command3 = (["TripleInOne", "peek", "pop", "isEmpty", "push", "pop", "push", "push", "pop",
                 "push", "push", "isEmpty", "pop", "peek", "push", "peek", "isEmpty", "peek", "pop",
                 "push", "isEmpty", "pop", "peek", "peek", "pop", "peek", "isEmpty", "pop", "push",
                 "isEmpty", "peek", "push", "peek", "isEmpty", "isEmpty", "isEmpty", "isEmpty", "peek",
                 "push", "push", "peek", "isEmpty", "peek", "isEmpty", "push", "push", "push", "peek",
                 "peek", "pop", "push", "push", "isEmpty", "peek", "pop", "push", "peek", "peek", "pop",
                 "isEmpty", "pop", "peek", "peek", "push", "push"],
                [[18], [1], [2], [1], [2, 40], [2], [0, 44], [1, 40], [0], [1, 54], [0, 42], [0], [1], [1],
                 [0, 56], [2], [0], [2], [2], [1, 15], [1], [1], [0], [2], [0], [0], [1], [0], [0, 32], [0],
                 [0], [0, 30], [2], [1], [1], [0], [0], [0], [0, 56], [1, 40], [2], [0], [0], [0], [2, 11],
                 [0, 16], [0, 3], [2], [0], [2], [0, 39], [0, 63], [1], [2], [0], [2, 36], [1], [0], [2], [1],
                 [0], [1], [2], [0, 8], [0, 38]])
    command4 = (["TripleInOne", "peek", "pop", "isEmpty", "push", "pop", "push", "push", "pop", "push", "push",
                 "isEmpty", "pop", "peek", "push", "peek", "isEmpty", "peek", "pop", "push", "isEmpty", "pop",
                 "peek", "peek", "pop", "peek", "isEmpty", "pop", "push", "isEmpty", "peek", "push", "peek",
                 "isEmpty", "isEmpty", "isEmpty", "isEmpty", "peek", "push", "push", "peek", "isEmpty", "peek",
                 "isEmpty", "push", "push", "push", "peek", "peek", "pop", "push", "push", "isEmpty", "peek",
                 "pop", "push", "peek", "peek", "pop", "isEmpty", "pop", "peek", "peek", "push", "push"],
                [[18], [1], [2], [1], [2, 40], [2], [0, 44], [1, 40], [0], [1, 54], [0, 42], [0], [1], [1],
                 [0, 56], [2], [0], [2], [2], [1, 15], [1], [1], [0], [2], [0], [0], [1], [0], [0, 32], [0],
                 [0], [0, 30], [2], [1], [1], [0], [0], [0], [0, 56], [1, 40], [2], [0], [0], [0], [2, 11],
                 [0, 16], [0, 3], [2], [0], [2], [0, 39], [0, 63], [1], [2], [0], [2, 36], [1], [0], [2], [1],
                 [0], [1], [2], [0, 8], [0, 38]])
    # [null,-1,-1,true,null,40,null,null,44,null,null,false,54,40,null,-1,false,-1,-1,null,false,15,56,-1,56,42,
    # false,42,null,false,32,null,-1,false,false,false,false,30,null,null,-1,false,56,false,null,null,null,11,3,
    # 11,null,null,false,-1,63,null,40,39,36,false,39,40,-1,null,null]

    def run(cmd):
        test = TripleInOne(cmd[1][0][0])
        for i, x in enumerate(cmd[0]):
            if x == 'push':
                test.push(cmd[1][i][0], cmd[1][i][1])
                ret.append(None)
            elif x == 'pop':
                ret.append(test.pop(cmd[1][i][0]))
            elif x == 'peek':
                ret.append(test.peek(cmd[1][i][0]))
            elif x == 'isEmpty':
                ret.append(test.isEmpty(cmd[1][i][0]))

    ret = [None]
    run(command3)
    print(ret)


if __name__ == '__main__':
    main()



# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)