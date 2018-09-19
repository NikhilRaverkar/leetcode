class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list=[]
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)
        if x< self.min:
            self.min=x


    def pop(self):
        """
        :rtype: void
        """
        if self.list[-1] == self.min:
            minval=float('inf')
            for i in range(len(self.list)):
                if i == len(self.list)-1:
                    continue
                val = self.list[i]
                if val <minval:
                    minval=val
            self.min=minval
        return self.list.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
if __name__ =="__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)

    print(obj.getMin())
    obj.pop()
    print(obj.top())

    print(obj.getMin())