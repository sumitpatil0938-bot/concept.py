# ==========================================
#             DAY 31 DECORATORS
# ==========================================
# To kya haal chal bhi log , welcome back to new lecture
# to aaj ka hamar new topic hai decorators bhaii kuch nahi aasan hai
# jaisa naam waise he kaam bhi karta hai, to shuru karte hai 
# bina kisi time pass kiye

# bass function acche se aana chahiye.


# ==========================================
# DECORATORS ???
# ==========================================
# --> Ek function hota hai jo kisis dusre function ki functionality ko change
#     ya improve karta hai bina uske original code ko badle.
# Simple -> function ko modify ya extend karne bina uske original code change kiye.

# real life example:
# socho tere pass ek mobile hai.
# ab tu uspar cover laga deta hai.
# Mobile ----> cover Lagaya ----> ab mobile aur safe ho gaya
# notice kar , mobile wahi hai 
# bass uske upar ek extra layer aa gayi ,
# decorator bhi exactly wahi same hai.
# function wahi rhata hai.
# uske upar extra functionality add ho jati hai.


# sabse pehle ye samjho
# pytho main function bhi ek object hota hai.

# matlab function ko 
# - varible mein store kar sakte hain.
# - dusre function mein bhej sakte hain.
# - return bhi kar sakte hain.

# example:
def hello():
    print("Hello")
a = hello
a()
# // Output ???

# Ye kaise chala ?? 
# step by step
# def hello(): --> function bana.

# a = hello --> Hamne function ka referance a mein store kar diya.

# a() --> ab a bhi hello ki tarah kaam kar raha hai.


# ==========================================
# FUNCTION KE ANDAR FUNCTION
# ==========================================
# example:
def outer():
    def inner():
        print("Sumit")
    inner()
outer()
# // Output ???
# print mein ek function ke andar dusra function bana sakte hain.
# ye decorator ke liye bohat important concept hai.


# ==========================================
# FUNCTION KO ARGUMENT KI TARAH PASS KARNA
# ==========================================
# example:
def hello():
    print("Jangyaa")
def display(fun):
    fun()
display(hello)


# yaha:
# hello --> ek function hai.
# aur usko hamne --> display()
# mein argument ki tarah bhej diya.


# ==========================================
# AB DECORATOR BANATE HAI
# ==========================================
# example:
def decorator(func):
    def wrapper():
        print("Befor Function")
        func()
        print("After Function")
    return wrapper
# // Output ???

# Ab isko aaram se samajhte hain.
# Step by Step
# pehle --> decorator(func) --> function aaya.
# uske andar --> wrapper() --> function bana.
# wrapper ke andar --> print("Before Function")
# fir --> func() --> call kiya.
# fir --> print("After Function")
# last main --> return wrapper --> kar diya


# ==========================================
# AB ORIGINAL FUNCTION
# ==========================================
def greet():
    print("Welcome sumit bro")
# decorator lagana
greet = decorator(greet)
greet()
# // Output ???


# ==========================================
# YE KAISE CHALA ???
# ==========================================
# step by Step
# original finction --> greet() --> decorator ne use wrap kar diya.

# Ab jab --> greet() --> call hua.
# to pehla --> Before function run hua.
# fir original ones --> greet() run hua.
# fir --> After function run hua.


# ==========================================
# [@]SYMBOL ???
# ==========================================
# python mein shortcut diya gaya hai.
# instead of 
# greet = decorator(greet)
# ham likhte hain.
@decorator
def greet():
    print("Hello")
# ye dono same hai.


# ==========================================
# COMPLETE EXAMPLE
# ==========================================
# example:
def decorator(func):
    def wrapper():
        print("Befor Function")
        func()
        print("After Function")
    return wrapper
@decorator
def hello():
    print("hello Sumit")
hello()
# // Output ???



# ==========================================
# USE OF DECORATOR
# ==========================================
# real project mein decorate ka use hota hai.
# - Login check
# - Authentication
# - Authorization
# - Timing Measure
# - Logging
# - Permission
# - Error handling

# har baar same code likhne ki zarurat nahi padti.
# Ek decorator banao.
# Aur jis function par chahiye uske upar laga do.


# ==========================================
# REAL LIFE EXAMPLE
# ==========================================
# example:
def login_required(func):
    def wrapper():
        print("Checking Login...")
        func()
    return wrapper
@login_required
def dashboard():
    print("Welcome dashboard")
dashboard()
# // Output ???
# real website main isi tarah login check hota hai


# ==========================================
# DECORATOR KO TAOD KAR SAMAJHO
# ==========================================
# Original Function -> Decorator -> Wrapper -> Extra code -> Original code -> Extra code
# ye hi poora decorator ka flow hai 


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
def hello():

    print("Hello")

a = hello

a()

# 2)
def show():

    print("Python")

def display(fun):

    fun()

display(show)

# 3)
def decorator(func):

    def wrapper():

        print("Start")

        func()

        print("End")

    return wrapper

@decorator
def test():

    print("Running")

test()

# 4) Decorator kis cheez ko modify karta hai ?

# 5) decorator lagane ke liye konsa symbol use hota hai ?


# ==========================================
# MINI PROJECT 
# ==========================================
def message(func):
    def wrapper():
        print("Program Started")
        func()
        print("Program Finished")
    return wrapper
@message
def calculate():
    print("Addition Completed")
calculate()


# Decorator = Kisi Function ki functionality ko bina uska original code badle extend ya modify karna.
# @decorator

# to finally aaj hamara day 31 decorator complete
# bahii sach bolu to aaj ka topic bohat aasan tha 
# aur jise samaj main nahi aaya na bahi sach main bola raha hu 
# function vaala lecture dekho matlabb revise karo ek baar acche se 
# aur daily ke daily revise karte jao 
# to milte hai day 32 main kisi new topic ke saath tab tak ke liye
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
