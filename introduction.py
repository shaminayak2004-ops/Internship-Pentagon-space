#Basic program
class fan:                             #class name
    def __init__(self):                #declaration of constructor
        self.brand="usha"
        self.color="white"
    def on(self):                     #method 1
        print("fan is on")
    def rotate(self):
        print("fan is rotating")          #method 2
    def off(self):
        print("fan is off")                #method 3
f1=fan()                                 #creation of object
print(f1.brand)
print(f1.color)
f1.on()
f1.off()
f1.rotate()
#organization of RAM
class heroine:
    def __init__(self):
        self.name="Rashmika"
        self.age=28
        self.numofmovies=5
    def act(self):
        print("she is crush of karnataka")
h1=heroine()
print(h1.name)
print(h1.age)
print(h1.numofmovies)
h1.act()
#add,modify,del variables
class hero:
    def __init__(self):
        self.name="vijay"
        self.age=30
        self.numofmovies=11
    def act(self):
        print("vijay is handsome")
h1=hero()
print(h1.name)
print(h1.age)
print(h1.numofmovies)
h1.act()
h1.movie_name="Taxi driver"               #add new variable
print(h1.movie_name)
h1.age=32                                 #update the variable
print(h1.age)
del h1.name                               #deleting variable
print(h1.name)    #will get error,once deleted finished
#self keyword, reference variable have sa,e address
class car:
    def __init__(self):
        self.brand="tata"
        self.color="blue"
    def start(self):
        primt("car has started")
        print(self.color)
        print(self)
c1=car()
print(c1.brand)
c1.start()
print(c1)
