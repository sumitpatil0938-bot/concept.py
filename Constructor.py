# ==========================================
#            DAY 24 CONSTRUCTOR
# ==========================================

# to kya haal chaal bhi log kaise ho , welcome back to day 24.
# to aaj ka hamara topic hai constructor ,
# haa jise hamne day 23 main padha tha , 
# pr aaj hamn usee aur acche se samjenge .
# To shuru karte hai bina kisi time pass kiya 


# ==========================================
# CONSTRUCTOR
# ==========================================
# --> constructor rk special method hota hai.
# ye object creat hote hi automatically run ho jata hai.
# samjata hu 
# s1 = Student() --> object creat hua
# __init__() --> constructor khud se run ho gaya 
#                hame call nai karna padta

# REAL LIFE EXAMPLE:
# soch tu ek student ka form bhar raha hai.
# hab bhi naya student aata hai Name, Age, City
# ye information fill karni padti hai.
# OOP mein constructor isi initial information ko set karne ke liye use hota hai.

# syntax: 
class student:
    def __init__(self):
        print("constructor called")
s1 = student()

# example.
class student:
    def __init__(self):
        print("Student created")
s1 = student() # // Output ???

# ab ise run karo ? ho jayega 
# pr tumne socha hamne to ise call he nahi kiya to run kaise hua 
# ha to ye hi hota hai 
# object creat hote hi python ise automatically run karta hai.


# ==========================================
# MULTIPLE OBJECTS 
# ==========================================
# kya hota hai multiple object , ye to hamne day 23 main cover kiya 
# aaj firse karte hai
# example
class Student:
    def __init__(self):
        print("Sumit")
s1 = Student()
s2 = Student()
s3 = Student()

# // Output ???

# yaha pe hamne multiple object creat kiya hai 
# object matlab s1,s2,s3 ise ham object bolte hai 
# har object ke saath constructor ek baa run hua


# ==========================================
# CONSTRUCTOR ME DATA STORE KARNA 
# ==========================================
# example.
class mobile:
    def __init__(self,name):
        self.name = name
m1 = mobile("Apple")
print(m1.name)
m2 = mobile("Samsung")
print(m2.name)
m3 = mobile("Micromax")
print(m3.name)
m4 = mobile("1+")
print(m4.name)

# // Output ???

# Step by Step
# m1 = mobile("Apple") --> object bana 

# python ne:
# __init__("Apple") --> run kiya 

# self.name = name 
# name main isne 
# self.name = "Apple"
# store kar diya 

# call karte hi hame output mil gaya.
# ab tu bolega hamne to yaha pe call kiya hai aur aapne bola call nahi karna pdta ?? 
# agar tu code dekhega to tuje samaj main aayega 
# dekho yaha pe constructor ne name = apple data save to kar liya hai 
# pr hame wo data dekhne ke liye print karna hota hai
# to hame pata hai apple jo hamar data hai wo name main save hai
# to tum khud se dekh lo hamne name ko print kiya hai , okay 
# aur same waise he 
# upar vaala multiple object 
# us main hamne 
# call nahi liya aur na hi print kiya hai 
# jo print("sumit") hai wo hamne data save kiya hai s1 = student main


# ==========================================
# MULTIPLE PARAMETER
# ==========================================
# example.
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = student("mangesh",20)
print(s1.name)
print(s1.age)
# // Output ???

# parameter matlab name,age, jo bhi ham add karna chahate hai use ham parameter bole hai.


# ==========================================
# CONSTRUCTOR + METHOD
# ==========================================
class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name)
        print(self.age)

s1 = student("sumit",20)
s1.show()
# // Output ???

# ham without constructor ka bhi kar sakte hai 
class student:
    pass
s1 = student()
s1.name = "rohan"
s1.age = 21
print(s1.name)
print(s1.age)

# pr tu soch agar tuze rohan ki aur detail add karni ho
# to tu kya saare ke liye ek ek banate firega 
# s1.name = "rohan"
# s1.age = 21
# s2.name = "sumit"
# s2.age = 21
# usee accha ek barr main baan lo aur usmi kini bhi student ka data add kar do
# is liye ham oop ka use karte hai  


# ==========================================
# DEFAULT CONSTRUCTOR
# ==========================================
# ab tune multiple object vaal code to dekha hoga
# hamne waha pe parameter ka use nahi kiya 
# bass wahi baat hai 
# defaulit constructor ka matlab hai han usme parmeter ka use nahi karte 
# example.
class student:
    def __init__(self):
        print("jangyaa")
s1 = student()


# ==========================================
# PARAMETERIZED CONSTRUCTOR
# ==========================================
# matlab jis main ham parameter ka uswe karte hai 
# jaise ham ab tak karte aarahe hai 
# exmaple.
class animal:
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat
    
    def show(self):
        print(self.name)
        print(self.habitat)

a1 = animal("fish","water")
a2 = animal("horse","stable")
a3 = animal("king","den")
a1.show()
a2.show()
a3.show()

# ismai name,habitat parameter hai 


# ==========================================
# SELF ??
# ==========================================
# abhi tak ham ise use karte aa rahe the
# to ab ham ise samjte hai self kya hota hai 
# kyu use karte hai
# example.
class animal:
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat
    
    def show(self):
        print(self.name)
        print(self.habitat)

# run mat kar error aayega aadha he code hai na 
# isk use ham 
# object ko store karne ke liye karte hai 

# agar :
# s1.student("sumit")
# to self ke help se 
# self.name = "sumit"
# ho jayega 


# ==========================================
# PRACTICE TIME 
# ==========================================
# 1)
class Student:

    def __init__(self):
        print("Hello")

s1 = Student()

# 2)
class Person:

    def __init__(self,name):
        self.name = name

p1 = Person("Rahul")

print(p1.name)

# 3)
class Car:

    def __init__(self,brand):
        self.brand = brand

c1 = Car("BMW")

print(c1.brand)

# 4)
class Mobile:

    def __init__(self,name,price):

        self.name = name
        self.price = price

m1 = Mobile("iPhone",80000)

print(m1.price)

# 5)
class Student:

    def __init__(self,name):

        self.name = name

    def show(self):

        print(self.name)

s1 = Student("Sumit")

s1.show()


# ==========================================
# MINI PROJECT
# ==========================================

name = input("Enter Name : ")
age = int(input("Enter Age : "))
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("Name = ", self.name)
        print("Age = ",self.age)
s1 = student(name,age)
s1.show()


# To finally aaj hamar day 24 constructor khatam 
# aaj hamne constructor ko acche se samjha 
# ye oop ka he ek chota sa part hai jiase hamne detail main samja
# to agle 2-3 din ham oop ko aue acche se samjte hai 
# tab tak ke liye ise acche se aur practise karo 
# to milte next lecture main 
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳