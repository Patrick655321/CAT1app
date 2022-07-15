import sys


class Staff:
    def __init__(self, role, mon, tue, wed, thur, fri, sat, sun):
        self.role = role
        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thur = thur
        self.fri = fri
        self.sat = sat
        self.sun = sun

class Shift:
    def __init__(self, [day], [night])

staff_list = ["Moe", "Grace", "Judith", "Luane", "Fausto", "George", "Paul", "Mykel", "Mustafa", "Maddison", "Allie"]

Moe = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Grace = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Judith = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Luane = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Fausto = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
George = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Paul = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Mykel = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Mustafa = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Maddison = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")
Allie = Staff("mgr", "both", "both", "both", "both", "both", "both", "both")

mon = {
    "mgr" : 1,
    "bar" : 1,
    "rest" : 2,
}

totals = ("Mon", mon["mgr"]+mon["bar"]+mon["rest"])

print(totals)