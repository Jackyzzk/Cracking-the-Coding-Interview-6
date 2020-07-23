class MyQueue(object):
    """
实现一个MyQueue类，该类用两个栈来实现一个队列。
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.que.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.que.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.que[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.que else True


def main():
    command1 = (["MyQueue","push","push","peek","pop","empty"], [[],[1],[2],[],[],[]])
    command2 = (["MyQueue","empty"], [[],[]])  # [null,true]

    def run(cmd):
        test = MyQueue()
        for i, x in enumerate(cmd[0]):
            if x == 'push':
                test.push(cmd[1][i][0])
                ret.append(None)
            elif x == 'peek':
                ret.append(test.peek())
            elif x == 'pop':
                ret.append(test.pop())
            elif x == 'empty':
                ret.append(test.empty())

    ret = [None]
    run(command2)
    print(ret)


if __name__ == '__main__':
    main()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()