# ==========================================
#             DAY 18 RECURSION
# ==========================================

# To welcom back guyss to aaj hai hamar day 18 aur aaj ka hamar topic hai recursion , 
# to ye topic ko ham detail main padne vaale hai jaise ham daily padte hai.
# chota topic hain bass concept samj ja acche se okay.
# shuru karte hai bina kisi time pass kiye.


# ==========================================
# RECURSION
# ==========================================
# --> jab koi function khud ko hi call karta hai . kaise wo mai bata ta hu acche se example ke saath.
# example
def hello():
    print("hello")
    hello()
hello() # // Output ???

# output check mat kar infinite loop chal jayega aue baad main apne aap error dedeg.
# aaram se dekh samja ta hu.

# ab kya hoga ?
# hello() --> call hua 
# function ke andar gaya.

# print("hello") --> print hua.
# fir niche.

# hello() --> firse call hua 
# firse function ke andar gaya

# fir print("hello") --> print hua 
# fir hello() --> firse call hua 

# aur ye chalta he rahega.
# infinit barr. last main python error de dega.


# ==========================================
# BASE CONDITION
# ==========================================
# base condition recursion ko rokne ke liye use hota hai.
# agar base condition na ho to recursion kabhi nahi rukhega chalta he jayega aur last main erroe de deg .
# example.
def count(num):

    if num == 5:
        return
    print(num)
    count(num + 1)
count(1) # // Output ???

# Step by step samjte hai acche se .

# count(1) -->  call hua

# num = 1 --> function ke andar gaya
# check if 1 == 5 --> nahi (False)

# to ab print(1)
# ab count(1+1) = count(2) --> count(2) call hua 

# abe ye count(2) count(1) ke taraf nahi aayega matlab count(2) niche nahi aayega 
# ab ye loop upar ke upar he chlta rahega , tab tak jab tak ye 
# if main num(5) == 5 nahi hoga 
# if num(5) == 5 , True --> return 

# function ruk gaya 
# ab function infinit nahi chala 


# ==========================================
# RECURSION VS LOOP
# ==========================================
# Loop --> example.
for i in range(1,6):
    print(i) # // Output ???

# Recursion --> example.
def print_num(num):

    if num > 5:
        return
    print(num)
    print_num(num + 1)
print_num(1) # // Output ???

# same output milega 
# ab tu bolega to loop kyu nahi use karte , recursion kyu?
# loop ka ocde bhi easy hai aur output bhi same ,
# tuzje abhi nahi samaj aayega aage jake khud ba kud samjega .


# ==========================================
# COUNTING - TO -
# ==========================================
# example.
def count(num):
    if num > 10:
        return
    print(num)
    count(num + 1)
count(1) # // Output ???

# deka aaram se dekh aur samaj upar maine jo logic batay wahi logic hain 
# bass maine yaha pe condition change ke hai 
# num == 5 ko num > 10 kiya hai , okay 


# ==========================================
# COUNTDOWN - TO -
# ==========================================
# example.
def countdown(num):
    if num == 0:
        return
    print(num)
    countdown( num - 1 )
countdown(30) # // Output ???

# isme hamne kuch nahi kiya 
# ham countdown kaha pe khatam hona chayetha 0 pe 
# islye hamne num == 0 
# jab num == 0 --> true aayega tab return ho jayega 
# so ham countdown kar rahe hai matlab ek number subtract hota jayega 
# to islye hamne countdown( num - 1 ) --> taaki ek number subtract hota jaye har ek count mai.
# aur jaha se shuru karna hai waha pe bass call karte time number daal do .


# ==========================================
# FACTORIAL[!] USING RECURSION
# ==========================================
# factorial matlab 
# 5! = [5 * 4 * 3 * 2 * 1]

# ye vaala recursion k sabse famous example hai bahiiii loggggg.
# example.
def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)
print(factorial(5))

# to cahlo ise samjte hai Step by Step
# print(factorial(5)) --> call hua 

# factorial(num) --> factorial(5)

# return num == 1 main to nahi jayega kyu ki 
# num == 1 or num kya hai 5 
# 5 == 1 , False 

# to ab,
# next return main 
# num * factorial(num - 1) --> 5 * factorial(5 - 1) --> 5 * factorial(4)
# return 
# num * factorial --> 5 * 4 * factorail(3)

# aise tabb tak chalge ja tak
# num * factorial(num - 1) --> 5 * 4 * 3 * 2 * 1

# Last maine
# num == 1 --> 1 == 1 , True

# // Output ???


# ==========================================
# RECURSION KE RULE 
# ==========================================
# har recursion main 2 cheeze honi chahiye

# 1) BASE CONDITION
# --> if num == 0: 
#        return
# ye sab jaisa aapka code hai uske hisab se lo condition ,pr ye code main rehna chahiye .

# 2) RECURSIVE CALL
# --> count(num-1) according to your code condition likho .


# agar ek bhi missing raha to galat ho jayega 


# ==========================================  
# PRACTICE QUESTION
# ==========================================

# 1) 
def show():
    print("Hello")
    show()

show()


# 2)
def count(num):

    if num > 3:
        return

    print(num)

    count(num + 1)

count(1)

# 3)
def countdown(num):

    if num == 0:
        return

    print(num)

    countdown(num - 1)

countdown(3)

# 4)
def test(num):

    if num == 4:
        return

    print(num)

    test(num + 1)

test(1)

# 5)
def factorial(num):

    if num == 1:
        return 1

    return num * factorial(num - 1)

print(factorial(7))


# ==========================================
# MINI PROJECT
# ==========================================

# Q) user se number lo aur recursion se countdown print karo
num = int(input("enter number : "))
def countdown(num):
    
    if num == 0:
        return 
    print(num)
    countdown(num-1)

countdown(num)

# To finally aaj ka hamara day 18 recursion khatam bahii aasan hai bass practice kar le , dekh aage aane wali saare ke saare topic aise he hai 
# to abse tuze theory nahi milge abse tuze bass example solve karne ahi aur samjne hai kaise hua aur kyu 
# logic samjte ja saara khel logic pr hai aage aane vaale lectures main , to dhya se practice kr leo 
# to milte kal kisi new topic ke saath day 19 main tab tak ke liye 

# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳

