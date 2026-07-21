# ==========================================
#           DAY 26 POLYMORPHISM
# ==========================================
# welcome back to our new lecture.
# to aaj hai hamar day 26 jis main ham padhne ja rahe hai
# polymorphism ko detail main.
# bhai log sach main bolu to aaj ka bohat aasan topic hai 
# to shuru karte hai bina kisi time pass kiya 


# ==========================================
# POLYMORPHISM
# ==========================================
# --> poly = many
#     morphism = Forms
# Ek hi cheez alag alag tarike se kaam karna.
# example.
# Dog -> sound -> Bark
# Cat -> sound -> Meow
# cow -> sound -> Moo
# sab animals he hai , pr sabke pass.
# sound() common hai.
# yehi polymorphism hai.

# example.
print(len("sumit")) # // Output ???
print(len([10,20,30])) # // Output ???

# yaha len() same function hai.
# par "Sumit" aur [10,20,30] pr alag alag kaam kar raha hai.
# ye bhi polymorphism hai.


# ==========================================
# METHOD OVERRIDING
# ==========================================
# ye is lecture ka imp concept hai.
# imp hai pr hard one nahi 

# PARENT CLASS:
class animal:
    def sound(self):
        print("Animal Sound")
a1 = animal()
a1.sound()
# // Output ???

# CHILD CLASS:
class Dog(animal):
    def sound(self):
        print("bark")
d1 = Dog()
d1.sound()
# // Output ???

# COMPLETE EXAMPLE 1:
class animal:
    def sound(self):
        print("Animal sound")
class cat(animal):
    def sound(self):
        print("Meow")
c1 = cat()
c1.sound()
# // Output ???

# Ab dekh parent ke andar bhi sound() hai.
# child ke andar bhi sound() hai.
# python child wali method use karega.
# isko method overriding bolte hai.
# ye polymorphism ka example hai.

# Step by Step
# c1 = cat() --> object banadiya.

# c1.sound() --> python cat class mein sound() dhundega.
# mil gaya --> run karega. --> print wala ignore ho jayega


# ==========================================
# MULTIPLE CLASSES
# ==========================================
class man:
    def work(self):
        print("Working")

class women:
    def work(self):
        print("House Wife")

class son:
    def work(self):
        print("Studying")
m1 = man()
w1 = women()
s1 = son()

m1.work()
w1.work()
s1.work()
# // Output ???

# same --> work() method.
# par yaha class ka behaviour alag.
# yehi polymorphism hai.


# ==========================================
# TOD KAR SAMJNA 
# ==========================================
# work() --> ek naam hai.

# lekin:
# Man -> Working
# Women -> House Wife
# Son -> Studying

# same method.
# difference behaviour.
# isi ko ploymorphism bolte hai.


# ==========================================
# OPERATORS POLYMORPHISM
# ==========================================
# ye bhi interesting hai.
# example.
print(10 + 20) # // Output ???
print("Sumit" +" "+ "Love" + " "+ "Python") # // Output ???
# same operator [ + ]
# lekin dhya se dekho :
# Numbers -> add
# String -> join
# dono ke behaviour main differenc hai par fir bhi 
# ye polymorphism haii mere dost


# ==========================================
# INHERITANCE + POLYMORPHISM
# ==========================================
# example.
# bahi iska example hamne complete example 1 main dekha tha.
# fir bhi dobara likte hai ise 
class person:
    def sumit(self):
        print("I am person")
class student(person):
    def sumit(self):
        print("I am student")
q1 = student()
q1.sumit()
# // Output ???

# python child wali method ka use karega.
# kyuki usne parent wali method ko override kar diya.


# ==========================================
# PRACTICE TIME BRTHR/SISTARSS
# ==========================================
# 1)
class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Bark")
d1 = Dog()
d1.sound()
# // Output ???

# 2)
class Animal:
    def sound(self):
        print("Animal")

class Cat(Animal):
    def sound(self):
        print("Meow")
c1 = Cat()
c1.sound()
# // Output ???

# 3)
print(len("Python")) # // Output ???

# 4)
print(5 + 10) # // Output ???

# 5)
print("Hello" + " World") # // Output ???


# ==========================================
# PROJECT
# ==========================================
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d1 = Dog()
c1 = Cat()

d1.sound()
c1.sound()
# // Output ???


# Polymorphism = Same Method Name, Different Behavior

# bhaii log bola tha na aaj ka topic aasan hai kuch nahi.
# bass samj le aur practice kar taaki tu aur acche se samaj sake
# aur ha ummm... kuch nahi jne de .
# milte hai agle lecture main kisi new topic ke saath tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳