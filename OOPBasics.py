# ==========================================
#              DAY 23 OOP BASICS
# ==========================================
# to kya haal chal bhai log day 23 main swaagat hai aap sabka 
# aaj ham padhne ja rahe hai day 23 oop(Object Oriented Programming)
# naam thoda bada aur dangerous lag raha hoga par aasan hai 
# easy hai real life example se samajhna hoga to aurr bhi assan lagega
# to shuru karte hain bina kisi time pass kiye 


# ==========================================
# OOPS 
# ==========================================
# abhi tak ham variable bana rahe the:
name = "sumit"
age = 20
city = "pusad"

# yaha pe 1 student ka hai is liye hamne aise kiya 
# soch agar 100-200 student ho to kaise karega ??
# iske liye ham OOP ka use karte hai

# example.
# Har student ke pass:
# Name
# Age
# City
# ye information hoti hai
# Aur kuch kaam bhi kar sakta hai:
# Study
# Play
# Attend class

# To OOP main:
# Information = Attributrs
# Kaam = Methods


# ==========================================
# CLASS BANANA (BLUEPRINT)
# ==========================================
# class ko ham blueprint bolte hain
# syntax: class ClassName:
#              pass

# example.
# class student:
#     pass

# yaha hamne student naam ki class bana di.
# abhi iski andar kuch bhi nahi hai.


# ==========================================
# OBJECT KYA HOTA HAI ?
# ==========================================
# object matlab class ka actual instance.
# example.
class student:
    pass
s1 = student()
# yaha 
# s1 --> ek object hai.


# ==========================================
# EK SE JYADA OBJECT ?
# ==========================================
# example.
class Student:
    pass
s1 = Student()
s2 = Student()
s3 = Student()



# ==========================================
# INIT() METHOD
# ==========================================
# ab object ke andar data store karne ke  
# liye use hota hai:

# code --> __init__()

# isko CONSTRUCTOR bolte hain.
# ye object creat hote hi automatically run hota hai
# example.
class Student:

    def __init__(self):
        print("Student Created")

s1 = Student() # // Output ???


# ==========================================
# SELF
# ==========================================
# ye OOP ka sabse important concept hai.
# abhi ke liye bass itna yaad rakho
# Self current object ko represent karta hai.
# example se samaj.
# hamne niche vaale example main self ka use kiya hai.


# ==========================================
# DATA STORE KARNA
# ==========================================
# example.
class Student:

    def __init__(self , name):
        self.name = name
s1 = Student("Sumit")
print(s1.name) # // Output ???

# Step by Step
# code --> s1 = Student("Sumit")
# object creat hua.

# self.name = name
# main python ne:
# s1.name ="Sumit"
# store kar diya 

# print(s1.name)
# output:
# Sumit


# ==========================================
# MULTIPLE VALUES STORE KARNA 
# ==========================================
class Student:

    def __init__(self,name,age):

        self.name = name
        self.age = age

s1 = Student("Sumit",21)

print(s1.name)
print(s1.age) 
# // Output ???


# ==========================================
# METHOD KYA HOTA HAI
# ==========================================
# class ke andar function ko method bolte hain.
# Method class ke andar bana hua function hota hai,
# aur object ke through use kabhi bhi call karke 
# us object par action perform kar sakte hain.

# example 1.
class student:
    
    def __init__(self,name):
        self.name = name
    
    def show(Self):
        print(Self.name)

s1 = student("Sumit")
s1.show()
# // Output ???


# example 2.
class student:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)
s1 = student("sumit")
s1.show()
print("Sumit is good boy") # samjlo yaha pe bich main tumhara code hai 
s1.show()
s1.show()
# // Output ???


# example 3.
class student:
    def __init__(self,name):
        self.name = name
    def change_name(self,new_name):
        self.name = new_name
    def show(self):
        print(self.name)
s1 = student("Sumit")
s1.show()
s1.change_name("Ved")
s1.show()
# // Output ???

# yaha pe 
# show() --> method
# change_name --> method
# dono ko code mein alag-alag jagah par call kiya gaya hai
# method ko class ke andar define karte hain.
# aur object ke through call karte hain.


# ==========================================
# REAL EXAMPLE
# ==========================================
class student:

    def __init__(self,name,age):

        self.name = name
        self.age = age
    
    def show(self):
        print("Name =" , self.name)
        print("Age =" , self.age)
s1 = student("jangyaa",19)
s1.show()


# ==========================================
# OOP KO TOD KAR SAMAJHO
# ==========================================
# code --> class student:
# class(blueprint) bani.

# code --> def __init__(self,name,age):
# object creat hote hi run hoga.

# code --> self.name = name
# Name save hua.

# code -->self.age = age
# age save hua.

# s1 = student("Sumit",21)
# object bana.

# code --> s1.show()
# method call hua.


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
class Car:
    pass
c1 = Car()
print(type(c1))

# 2)
class student:
    def __init__(self,name):
        self.name = name
s1 = student("rahul")
print(s1.name)

# 3)
class person:

    def __init__(self,age):
        self.age = age
p1 = person(25)
print(p1.age)

# 4)
class mobile:

    def __init__(self,brand):
        self.brand = brand
m1 = mobile("Apple")
print(m1.brand)

# 5)
class student:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)
s1 = student("sumit")
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
        print("Name = " , self.name)
        print("Age = " , self.age)

s1 = student(name,age)
s1.show()


# to finally aaj hamar day 23 khatam , to aaj hamne oop ka basics padha hai
# to aage ke lectures main ham isko detail mai padhenge kya hota hai oop 
# abhi focus sirf class + object + self + init() + method
# to milte hai day 24 main , tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳







