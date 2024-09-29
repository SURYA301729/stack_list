class STACK:
    def __init__(self,n):
        self.size=n
        self.li=[]
    def push(self,value):
        if len(self.li)==self.size:
            print("overflow")
        else:
            self.li.append(value)
    def Pop(self):
        if self.li==[]:
            print("no element")
        else:
            return self.li.pop()
    def peak(self):
        if self.li==[]:
            print("no element")
        else:
            return self.li[-1]
    def print(self):
        print(self.li)
obj=STACK(5)
obj.push(9)
obj.push(7)
obj.push(5)
obj.push(4)
obj.push(2)
obj.Pop()
var1=obj.peak()
obj.print()
print("peak_value",var1)

