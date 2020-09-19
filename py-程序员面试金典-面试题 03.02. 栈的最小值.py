class MinStack(object):
    """
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，
该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
链接：https://leetcode-cn.com/problems/min-stack-lcci
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = []
        self.seq = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)
        if x <= self.seq[-1]:
            self.seq.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.que.pop() == self.seq[-1]:
            self.seq.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.que[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.seq[-1]


def main():
    command1 = (["MinStack","push","push","push","getMin","pop","top","getMin"],
                [[],[-2],[0],[-3],[],[],[],[]])
    command2 = (["MinStack","push","push","push","getMin","pop","getMin"],
                [[],[0],[1],[0],[],[],[]])  # [null,null,null,null,0,null,0]

    def run(cmd):
        test = MinStack()
        for i, x in enumerate(cmd[0]):
            if x == 'push':
                ret.append(test.push(cmd[1][i][0]))
            elif x == 'getMin':
                ret.append(test.getMin())
            elif x == 'pop':
                ret.append(test.pop())
            elif x == 'top':
                ret.append(test.top())

    ret = [None]
    run(command2)
    print(ret)


if __name__ == '__main__':
    main()



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()