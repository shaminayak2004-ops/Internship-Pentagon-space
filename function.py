#function syntax/#no parameter no return value
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
#types of function
#no parameter with return type
def add():
    a=10
    b=20
    c=a+b
    return(c)
res=add()
print(res)
#with parameter no return type
def add(a,b):
    c=a+b
    print(c)
x=3
y=4
add(x,y)
#with parameter with return type
def add(a,b):
    c=a+b
    return(c)
x=3
y=4
res=add(x,y)
print(res)
#invoking function threough variable
def fun1():
    print("inside fun1")
def fun2:
    print("inside fun2")
ptr1=fun1
ptr2=fun2
ptr1()
ptr2()
#ASCII Values
#alpha->num
alpha=input("enter the alpha")
res=ord(alpha)
print(res)
#num->alpha
num=input("enter the num")
res1=chr(num)
print(res1)
#nested ()
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    inner()
outer()
#higher order() &1st class ()
def fun1():
    print("inside fun1")
def fun2():
    print("entering fun2")
    ptr()
    print("leaving gun2")
fun1()
fun2(fun1)
#global variables
a=10
def fun():
    a=100
    b=200
    print(a)
    print(b)
def fun():
    c=300
    print(a)
    print(c)
fun1()
fun2()
#accesing and modifying global variables
a=100
def fun1():
    global a
    a=10
    b=20
    print(a)
    print(b)
def fun2():
    global a
    a=15
    b=25
    print(a)
    print(b)
    print(a)
fun1()
print(a)
fun2()
print(b)
#Non local  accessing modiyfing non local variables
def outer():
    a=100
    b=200
    print(a)
    print(b)
    def inner():
        nonlocal a
        a=150
        b=250
        print(a)
        print(b)
        print(a)
    inner()
    print(a)
outer()
#lambda ()
def square(num):
    return num*num
    l=lambda num:num*num
    res=l(7)
    print(res)
#function workflow
def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        c=15
        print(a)
        print(c)
    inner()
outer()
#closure in nested ()
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
        return inner
ref=outer()
ref()
#MODULUS
#prgm1.py
def fun1():
    print("inside fun1")
#new.py
from prgm1 import fun1
fun1()
#FILTERING WITH LAMBDA ()
i=0
while i<=4:
    num=int(input("enter num"))
    L.insert(i,num)
    i=i+1
    print(L)
res=list(filter(lambda num=num%2==0,L))
print(res)
#MAPPINF WITH LAMBDA()
def add(num):
    return num+10
    L=[]
    i=0
    while i<=4:
        num=int(input("enter num"))
        L.insert(i,num)
        i=i+1
        print(L)
res=list(map(lambda num,num+10))
print(res)
#DECORATORS
def main():
    str="cartoon"
    return str
def outer(ptr):
    print("inside outer")
    def inner():
        print("entering inner")
        res=ptr()
        ans=res.upper()
        print(ans)
        print("leaving inner")
    return inner
    ref=outer(main)
ref()
#GENERATORS
def generator():
    yield 1
    yield 2
    yield 3
res=generator()#creating obj for generator
print(res)
print(next(res))
print(next(res))

