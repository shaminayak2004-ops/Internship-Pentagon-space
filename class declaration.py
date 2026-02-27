#standard way declaring class:
class student:
    def __init__(self):
        self.sname=name
        self.susn=usn
        self.sage=age
s1=student("shami",500,21)
s2=student("srushti",450,18)
print(s1.sage)
print(s2.sname)
#variousnway to declare instance variable
# 1)declaring inside class and inside constructor
# 2)declaring inside class and inside method
# 3)declaring outside the class
class chair:
    def __init__(self):
        self.brand="havell"           #rule1
        self.color="brown"            #rule1
    def rotate(self):
        self.cost=700                 #rule2
        print(self.cost)              #rule2
c1=chair()
print(c1.brand)
print(c1.color)
print(c1.cost)
c1.rotate()
print(c1.cost)
c1.material="wooden"                  #rule3
print(c1.material)
#concept of static variable(declared inside class, outside constructor)
class farmer:
    r=2.5                           #declaration of static variable
    def __init__(self):
        self.principle=p
        self.time=t
    def loan(self):
        si=(self.principle*self.time*farmer.r/100)
        print(si)
f1=farmer(p:20000,t:3)
f2=farmer(p:40000,t:2)
f1.loan()
f2.loan()
print(farmer.r)                     #printing static variable