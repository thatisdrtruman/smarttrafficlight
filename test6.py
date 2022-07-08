#started at 4:00


class SmartTrafficLight:
    def __init__(self, s1, s2):
        self.orderlist=[]
        self.s1num=s1[0]
        self.s1name=s1[1]
        self.s2num=s2[0]
        self.s2name=s2[1]
        if self.s1num<self.s2num:
            self.orderlist.insert(0,self.s1name)
            self.orderlist.insert(0,self.s2name)
        elif self.s1num>self.s2num:
            self.orderlist.insert(0,self.s2name)
            self.orderlist.insert(0,self.s1name)
    def turngreen(self):
        if not self.orderlist:
            return None
        return self.orderlist.pop(0)

#test.describe('Example Test Cases')
t = SmartTrafficLight([42, 'Corporation Rd'], [72, 'George St'])
print(t.turngreen())
print(t.turngreen())
print(t.turngreen())
#test.assert_equals(t.turngreen(), 'George St')
#test.assert_equals(t.turngreen(), 'Corporation Rd')
#test.assert_equals(t.turngreen(), None)
u = SmartTrafficLight([42, 'Corporation Rd'], [42, 'George St'])
print(u.turngreen())
#test.assert_equals(u.turngreen(), None)
v = SmartTrafficLight([42, 'Blake Rd'], [30, 'Neven Ave'])
print(v.turngreen())
print(v.turngreen())
print(v.turngreen())
#test.assert_equals(v.turngreen(), 'Blake Rd')
#test.assert_equals(v.turngreen(), 'Neven Ave')
#test.assert_equals(v.turngreen(), None)