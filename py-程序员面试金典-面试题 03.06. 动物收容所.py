class AnimalShelf(object):
    """
动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。
在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，
或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。
请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。
允许使用Java内置的LinkedList数据结构。
enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。
dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。

 输入：
["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [], [], []]
 输出：
[null,null,null,[0,0],[-1,-1],[1,0]]

 输入：
["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
 输出：
[null,null,null,null,[2,1],[0,0],[1,0]]
收纳所的最大容量为20000
链接：https://leetcode-cn.com/problems/animal-shelter-lcci
    """
    def __init__(self):
        self.seq = []
        self.dog = []
        self.cat = []

    def enqueue(self, animal):
        """
        :type animal: List[int]
        :rtype: None
        """
        self.seq.append(animal[1])
        if animal[1] == 0:  # cat
            self.cat.append(animal[0])
        else:
            self.dog.append(animal[0])

    def dequeueAny(self):
        """
        :rtype: List[int]
        """
        if not self.seq:
            return [-1, -1]
        if self.seq.pop(0) == 0:  # cat
            return [self.cat.pop(0), 0]
        else:
            return [self.dog.pop(0), 1]

    def dequeueDog(self):
        """
        :rtype: List[int]
        """
        if not self.dog:
            return [-1, -1]
        for i, x in enumerate(self.seq):
            if x == 1:
                self.seq.pop(i)
                break
        return [self.dog.pop(0), 1]

    def dequeueCat(self):
        """
        :rtype: List[int]
        """
        if not self.cat:
            return [-1, -1]
        for i, x in enumerate(self.seq):
            if x == 0:
                self.seq.pop(i)
                break
        return [self.cat.pop(0), 0]


def main():
    command1 = (["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"],
                [[], [[0, 0]], [[1, 0]], [], [], []])  # [null,null,null,[0,0],[-1,-1],[1,0]]
    command2 = (["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"],
                [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []])  # [null,null,null,null,[2,1],[0,0],[1,0]]
    command3 = (["AnimalShelf", "dequeueCat", "dequeueCat", "dequeueAny", "dequeueDog", "dequeueCat", "enqueue",
                "dequeueAny", "enqueue", "dequeueCat", "enqueue", "dequeueCat", "dequeueAny", "dequeueAny",
                "enqueue", "dequeueDog", "enqueue", "dequeueCat", "dequeueDog", "enqueue", "dequeueCat",
                "dequeueCat", "dequeueDog", "enqueue", "dequeueDog", "dequeueCat", "dequeueDog", "dequeueAny",
                "dequeueCat", "dequeueAny", "enqueue", "enqueue", "dequeueDog", "dequeueAny", "dequeueDog",
                "dequeueCat", "enqueue", "dequeueAny", "enqueue", "enqueue", "dequeueDog", "dequeueAny",
                "dequeueAny", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny", "dequeueCat", "enqueue",
                "enqueue", "dequeueCat", "dequeueDog", "dequeueDog", "dequeueDog", "dequeueDog", "dequeueDog",
                "enqueue", "enqueue", "enqueue", "enqueue", "enqueue", "dequeueCat", "dequeueCat", "dequeueDog", "enqueue"],
                [[], [], [], [], [], [], [[0, 1]], [], [[1, 0]], [], [[2, 1]], [], [], [], [[3, 1]], [], [[4, 0]], [], [],
                 [[5, 0]], [], [], [], [[6, 0]], [], [], [], [], [], [], [[7, 1]], [[8, 1]], [], [], [], [], [[9, 1]], [],
                 [[10, 1]], [[11, 1]], [], [], [], [[12, 0]], [], [], [], [], [[13, 0]], [[14, 0]], [], [], [], [], [], [],
                 [[15, 1]], [[16, 1]], [[17, 0]], [[18, 1]], [[19, 1]], [], [], [], [[20, 1]]])

    def run(cmd):
        test = AnimalShelf()
        for i, x in enumerate(cmd[0]):
            if x == 'enqueue':
                test.enqueue(cmd[1][i][0])
                ret.append(None)
            elif x == 'dequeueCat':
                ret.append(test.dequeueCat())
            elif x == 'dequeueDog':
                ret.append(test.dequeueDog())
            elif x == 'dequeueAny':
                ret.append(test.dequeueAny())

    ret = [None]
    run(command2)
    print(ret)


if __name__ == '__main__':
    main()


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()