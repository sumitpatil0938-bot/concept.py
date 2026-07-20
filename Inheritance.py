# ==========================================
#           DAY 25 INHERITANCE
# ==========================================
# So welcome back to day 25 to aaj ka hamar toic hain inheritance 
# jese ham detail main samj te hai , bina kisi time pass kiye 
# aur ha aaj ka topic bohat aassan hai ,


# ==========================================
# INHERITANCE
# ==========================================
# --> Ek class dusri class ki properties aur methods use kar sakti hai.
# example se samja ta hu.
# Animal 
# Dog
# Animal = Eat , Sleep
# Dog = Eat , Sleep
# dono kar sakte hai
# To dog ko do bara likhne ke jarurat nahi hai.
# Kyu ki dog bhi to animal he hai 
# Dog animal se inherit kar lega .
# Isi concept ko inheritance bolte hai 


# ==========================================
# INHERITANCE KA USE ?
# ==========================================
# socho:
class dog:
    def eat(self):
        print("Eating")

class cat:
    def eat(self):
        print("Eating")

# dono jagha same he code hai.
# fir yaha to duplicate code ho gaye.
# inheritance isi problem ko solve karta hai.


# ==========================================
# PARENT CLASS AND CHILD CLASS
# ==========================================
# Ye dono terms yadd rahkho imp hai.
# Parent class --> jisse properties milti hai.
# Child class --> jo properties leta hai.
# example.
class animal:
    pass

class dog(animal):
    pass

# Animal --> Parent class
# Dog --> Child class

# example.
class animal:
    def sleep(self):
        print("sleeping")
class tiger(animal):
    pass
t1 = tiger()
t1.sleep()

# Ab dekh hamne tiger class ke andar 
# def sleep(self) --> nahi likha 
# kyu ki tiger ne animal ko inherit kar diya.

# Step by Step
# class animal: --> parent class.

# class tiger(animal): --> tiger ne animal ko inherit kar diya.

# t1 = tiger() --> object creat hua.

# t1.sleep() --> tiger ke andar eat nahi mila
# python parent class(animal) ke andar gaya waha sleep mila
# output print ho gaya.

# dekh kitna simple hai , tu faltu fukat tension leta hai 
# chal jane de aage continue karte hai.


# ==========================================
# CHILD CLASS KI METHOD 
# ==========================================
# example.
class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("Barking")
d1 = dog()
d1.eat()
d1.bark()

# eat()--> parent se aaya.
# bark()--> dog ka khud ka method hai.


# ==========================================
# CHILD CLASS KI APNI VALUES
# ==========================================
# iska matlb bhi wahi same hota hai 
# khud ki values ya ni kahud ki method use karna.
# same example hai 

# dog parent ka bhi use kar sakta hai.
# aur apni bhi.


# ==========================================
# INHERITANCE + CONSTRUCTOR
# ==========================================
# kuch alag nahi hai wahi same hai. 
# isme ham ab constructor ka use karte hai ( __init__(self): )
# example.
class cars:
    def __init__(self):
        print("I Like Cars")
class tata(cars):
    pass
t1 = tata()

# tata ka constructor nahi tha.
# hamne cars ka constructor use kiya.


# ==========================================
# CHILD CLASS KA CONSTRUCTOR
# ==========================================
# ab child class khud ka aur parent clasa ka constructor use karega.
# example.
class cars:
    def __init__(self):
        print("I Love Cars")
class tata(cars):
    def __init__(self):
        print("My Favourite Car Company")
t1 = tata()


# ab yaha pe khud tata ka constructor mil gaya.
# to cars ka constructor run nahi hua 


# ==========================================
# ISS() FUNCTION
# ==========================================
# check karne ke liye use hota hai.
# output True ya false main aata hai.
# example 1.
class animal:
    pass
class dog(animal):
    pass
d1 = dog()
print(isinstance(d1,dog)) # // Output ???

# example 2.
class animal:
    pass
class dog(animal):
    pass
d1 = dog()
print(isinstance(t1,dog)) # // Output ???


# ==========================================
# REAL LIFE EXAMPLE
# ==========================================
# example.
class Man:
    def work(self):
        print("Working")
class student(Man):
    def study(self):
        print("Studying")
s1 = student()
s1.work()
s1.study()


# ==========================================
# OOP KO TOD KAR SAMAJHO
# ==========================================
# class man: --> parent class.

# class student(man): --> student ne man ko inherit kar diya.

# s1.work() --> man method.

# s1.study() --> student method.


# ==========================================
# PRACTICE TIME BOISSS/GRLSSS
# ==========================================
# 1)
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
d1 = Dog()
d1.eat()

# 2)
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    pass
c1 = Car()
c1.start()

# 3)
class Person:
    def walk(self):
        print("Walking")
class Student(Person):
    def study(self):
        print("Studying")
s1 = Student()
s1.study()

# 4)
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
d1 = Dog()
d1.bark()

# 5)
class Person:
    def walk(self):
        print("Walking")
class Student(Person):
    def study(self):
        print("Studying")
s1 = Student()
s1.walk()
s1.study()


# ==========================================
# MINI PROJECT
# ==========================================

name = input("Enter Name : ")
class person:
    def __init__(self,name):
        self.name = name
    def show(self):
        print("Name of student : ",self.name)
class student(person):
    def study(self):
        print("Studying Python Coding Language")
s1 = student(name)
s1.show()
s1.study()


# to finally aaj hamr day 25 khatam to aaj hamne padha 
# inheritance kya hota hai detail mai
# assan hai bhi bohat assan hai bass logic samjte 
# aage jake apne aap samjega 
# aurr ha practice karta ja aue clear hote jayege doubts
# to milte hain next lecture main kisi new topic ke saath 
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳