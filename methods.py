#Instance method
#no parameter no return value
class calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
c1=calculator()
print((c1.color))
print(c1.brand)
c1.add()
#no parameter with return value
class calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self):
        a=10
        b=20
        c=a+b
        return c
c1=calculator()
print(c1.color)
print(c1.brand)
res=c1.add()
print(res)
# with parameter no return type
class calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self,a,b):
        c=a+b
        print(c)
c1=calculator()
print(c1.color)
print(c1.brand)
x=10
y=10
c1.add(x,y)
#with parameter with return type
class calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self,a,b):
        c=a+b
        return c
c1=calculator()
print(c1.color)
print(c1.brand)
x=10
y=20
res=c1.add(x,y)
print(res)
#static method and class method
class mobile:
    def __init__(self):
        self.brand="samsung"
    def call(self):
        print("mobile is at call")
@staticmethod
    def charge():
        print("mobile is charging")
@classmethod
    def hang(cld):
        print("mobile is hanging")
m1=mobile()
print(m1.brand)
m1.call()
mobile.charge()
mobile.hang()
#method returing multiple values
class calci:
    def operations(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4
c=calci()
r1,r2,r3,r4=c.operations(5,2)
#actual parameters and formal parameters
class calculator:
    def __init__(self):
        self.color="black"
    def add(self,a,b):     #formal parameters
        c=a+b
        print(c)
c1=calculator()
x=5
y=10
c1.add(x,y)               #actual parameters
#default arguements and keyword arguements
class demo:
    def disp(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)
d1=demo()
x=11
y=22
z=33
d1=disp()
d1.disp(x.y,z)
d1.disp(z)
d1.disp(y,z)
d1.disp(b=z,a=y,c=x)
d1.disp(c=y)
