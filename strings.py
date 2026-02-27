# creation of string
#strings are stored in global dictionary
str="sita"
print(str)
for i in str:
    print(i)
    print(i,end="")               #end is used for output in single line
#Indexing
str="Babu"
print(str)
print(len(str))
print(str[-1])
print(str[-2])
print(str[0])
#arthimatic opeartion on strings
#opearators in string support only for +,*(with num only)
str1="shami"
str2="nayak"
str3=str1+str2
print(str3)                #concatenate strings
str4=str1-str2
print(str4)                #error 
str5=str1*str2
print(str5)                #error
str6=str1*2
print(str6)                
str7=str1/str2
print(str7)               #error
#string interning
str1="Loki"
str2="John"
str3="Loki"
str4="shaky"
str5="loki"
str6="rahul"
print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))
print(id(str6))
#string slicing
str="RajaRamMohanRoy"
print(str)
print(len(str))
print(str[2:7])
print(str[1:8:2])
print(str[-2:-6])
print(str[-2:-12:-3])
print(str[::2])
print(str[ : : ])
print(str[5:-2])
print(str[ : :-1])
print(str[5:-2])
#removing space at begin and end of string
str="Ramesh is drinking"
print(str)
str1=str.lstripe()
print(str1)
str2=str.rstripe()
print(str2)
str3=str.strip()
print(str3)
#reverse string
str=input("enter the string")
rev=""
for i in str:
    rev=i+rev
print(rev)
#reverse sentence
str="Ramesh is drinking"
rev=""
str1=str.split()
for i in str1
rev=i+""+rev
print(rev)
#palindrome
str=input("enter the string")
rev=("")
for i in str:
    rev=i+rev
print(rev)
if str==rev:
    print("palindrome")
else:
    print("not palindrome")
#checking whether string is alpha,numeric or both or other
str=input("enter the string")
print(str)
if str.isalpha():
    print("str is only alphabets")
elif str.isdigit():
    print("str only numbers")
elif str.isalnum():
    print("str contains both")
else:
    print("other")
#conversion of upper,lower,swapcase
str=input("enter a string")
print(str)
str1=str.upper()
print(str1)
dtr2=str.lower()
print(str2)
str3=str.swapcase()
print(str3)
#finding substring from given string
str="if you think you can or you cant,you are right"
print(str)
print(srt.count("you"))
str1="you"
print(str in str)
print(str.index("you"))
print(str.find("you"))
print(str.rindex("you"))
print(str.rfind("you"))
print(str.find("python"))
print(str.index("python"))
#replacing a substring
str="arju is dancing"
print(str)
str1=str.replace("is","was")
print(str1)
print(str.startswidth("arjun"))
print(stt.startswith("swamy"))
#packing and unpacking
str="rama"
print(str)
r1,r2,r3,r4=str
print(r1)
print(r2)
print(r3)
print(r4)
#string formating
name=input("enter a number")
print("hi" {}'.'format(name))