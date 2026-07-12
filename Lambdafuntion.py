# ==========================================
#         DAY 17 LAMBDA FUNCTIONS
# ==========================================

# To kya haal chaal bhai log kaise ho, firse swagat karta hu day 17 main.
# to aaj day 17 main ham padne ja rahe hai lambda function ke baare main wo bhi detail mai.
# aaj ka topic easy hai aur chota bhi hai

# abhi tak hamne normal function ko padha hai
# function kaise bante hain , function ko call karna kya hota hai ,
# ek barr 5 min main day 16 ko revise kar le taaki aaj ka topic aurr acche se samaj mai aaye 

# ==========================================
# LAMBDA FUNCTION
# ==========================================
# --> ye function ko likhne ka shortcut hai 
# expalin karta hu acche se .
# dekha lambda ek anonymous function hota hain
# anonymous ?? --> matlab jiska koi naam nai hota .
# ab tak ham function kuch aise bana rahe the 
def square(num):
    return num * num
print(square(9)) # // Output ???

# yaha pe function ka naam "square" hain
# pr lambda funtion mai ham direct function bana sakte hai without writing def , haa kar sakte hai waise 
#example.
square = lambda num : num * num
print(square(9)) # // Output ???

# dono ka output to same he aayega 
# to tu bolega ham lambda function ka use kyu karta hai ??
# kyu ki lamdba function kam code min same kaam karta hain
# aur jab function chota hota hai tab ham lambda function ka use karte hai .


# ==========================================
#  LAMBDA FUNCTION KA SYNTAX 
# ==========================================
# lambda parameter : expression 
# exmaple.
sumit = lambda num: num * 10
print(sumit(5))
# lambda --> keyword
# num --> parameter
# num * 10 --> expression
# sumit(5) --> "5" argument 
# expression ka result automatically return ho jata hain 
# isliye lambda function main return ki jarurat nahi hoti .


# ==========================================
# SINGLE ARGUMENT
# ==========================================
# example.
mangesh = lambda num: num + num
print(mangesh(1)) # // Output ???


# ==========================================
# MULTIPLE ARGUMENTS
# ==========================================
# example.
sumit = lambda a,b: a + b
print(sumit(10,10)) # // Output ???


# ==========================================
# THREE ARGUMENTS
# ==========================================
# example.
sahil = lambda a,b,c: a + b - c
print(sahil(10,20,5)) # // Output ???


# ==========================================
# LAMBDA FUNCTION WITH "STRING"
# ==========================================
# example.
Names = lambda name: "Hii" + name
print(Names("sumit")) # // Output ???


# ==========================================
# EVEN ODD CHECK
# ==========================================
# example.
even = lambda num : num % 2 == 0
print(even(10)) # // Output ???
print(even(9)) # // Output ???
# number even hai to True nahi to false 


# ==========================================
# GREATER NUMBER 
# ==========================================
# example.
greater = lambda a,b: a if a > b else b
print(greater(6,45)) # // Output ???


# ==========================================
# WORKING OF LAMBDA FUNCTION 
# ==========================================
# example.
square = lambda a,b: a * b
print(square(10,10))

# step by step chalte hai taaki acche se samj main aaye tuje

# print(square(10,10)) --> call hua (10,10) argument

# (a,b) parameter --> main value cahli gayi a aur b main 

# (a * b) expression --> ab wahi value jo parameter main gayi thi ab wo expression main gayi taki code run ho jaye .

# ab value 
# a * b
# 10 * 10

# 100 

# lambda function automatically 100 return karega 

# // Output ??? = 100


# ==========================================
# USER INPUT + LAMBDA FUNCTION 
# ==========================================
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
sumit = lambda num1,num2: num1 * num2
print(sumit(num1,num2)) # // Output ???


# ==========================================
# LAMBDA FUNCTION LIMITATIONS
# ==========================================
# lambda function main sirf ek expression likh sakte hain .
# bohat bada logic nahi 
# agar logic bada ho to hame normal function ka use karna padta hain , jo hamne day 16 main padha tha .
# example.

def calculate(a,b):
    total = a + b
    return total

print(calculate(10,5)) # // Output ???

# to aise case mai normal function best rehta hai 


# ==========================================
# PRACTICE QUESTION 
# ==========================================
# 1)
square = lambda num: num * num
print(square(3)) # // Output ???

# 2)
add = lambda a,b: a + b
print(add(5,5)) # // Output ???

# 3)
cube = lambda num: num*num*num
print(cube(3)) # // Output ???

# 4)
odd = lambda num: num % 2 == 1
print(odd(3)) # // Output ???

# 5) 
Name = lambda name: "I LOVE U" + " " + name
print(Name("sumit")) # // Output ???


# ==========================================
# MINI PROJECT 
# ==========================================
# user se naam lo aur lambda function ki help se welcome message print karo ??
# -->
name = input("Enter name : ")
xyz = lambda name: "Welcome" + " " + name
print(xyz(name))



# to finally aaj ka hamar mini topic lambda function kahatam assan hai bhaii practice kar ho jayega 
# to milte hai day 18 main kisi new topic ke saath , tab tak ke liye 

# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
