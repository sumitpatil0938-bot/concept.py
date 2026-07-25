# ==========================================
#             DAY 30 GENERATORS
# ==========================================
# Welcome back to day 30 , to kaise ho bahi log sab sahi 
# to aaj ka hamar topic hai generators , jis ham detail main samjte hai 
# koi na bro assan topic hai aaj ka , bass ke baar ke liye kal ka revise kar le 5min main
# taaki aaj ka lecture ham shuru kar sake
# kyuki aaj ka bohat important concept hai python ka
# to shuru karte hai bina kisi timepass kiye


# ==========================================
# WHAT ARE GENERATORS ???
# ==========================================
# ek special function hota hai jo values ko ek-ek karke rturn karta hai.
# matlab saari values ek saath memory mein nahi banata.
# jab zarurat hoti hai tab next value deta hai.


# ==========================================
# ITERATOR AUR GENERATOR DIFFERENACE
# ==========================================
# kal hamne ise acche se padha tha.
# iter()
# next()
# iterator manually banana padta tha.
# generator mein python khid iterator bana deta hai.
# matlab hamne alag se iter() likhne ke jarurat nahi hai.

# example.
# soch ek water tank hai.
# agar tu ek hi baar mein 1000 litre paani bharloge, to bohat space lagega
# lekin agar zarurat padne par sirf 1 litre nikalte jao.
# to memory bhi kam lagegi.
# generator bhi exactly yehi karta hai.
# ek - ek value deta rehta hai.


# ==========================================
# NORMAL FUNCTION
# ==========================================
# exmaple.
def number():
    return 1
print(number())
# // Output ???

# ye function baar baar alag values nahi de sakta.
# return aate he function kahatam ho jata hai.


# ==========================================
# GENERATOR FUNCTION
# ==========================================
# generator function mein.
# --> yield
# keyword use hota hai.
# example.
def number():
    yield 1
gen = number()
print(next(gen))
# // Output ???


# ==========================================
# YIELD ???
# ==========================================
# ye sabse imporatant concept hai.
# --> yield value return bhi karta hai aur function ko wahi par pause bhi kar deta hai.
# ye line bohat important hai.
# return aur yield mein yahi difference hai.


# ==========================================
# RETURN VS YIELD
# ==========================================
# Return:
def demo():
    return 10
    print("Hello")
# jaise hi return aaya , function wahi khatam.
# neeche ka code kabhi nahi chalega.

# Yield:
def demo():
    yield 10
    print("Hello")
# yaha function khatam nahi hota.
# pause hota hai.
# fir next() call karoge to wahi se continue karega.


# ==========================================
# MULTIPLE YIELD
# ==========================================
# example.
def sumit():
    yield 10
    yield 20
    yield 30
gen = sumit()
print(next(gen))
print(next(gen))
print(next(gen))
# // Output ???

# Step by Step
# generator function bana.
# gen = sumit() --> Object bana.

# next(gen) 
# pehle -> yield -> run hua.
# vlue 10 mili
# fir
# next(gen) -> dusra -> yield -> run hua.
# vlue 20 mili.
# fir
# next(gen) -> teesra -> yield -> run hua.
# value mili 30


# ==========================================
# RETURUN AUR YIELD DIFFERENCE 
# ==========================================
# Return: return
# function ko permanently khatam kar deta hai.

# Yield: yield
# function ko paus karta hai.
# Agli baar next() aayega to wahi se continue karega.


# ==========================================
# LOOP KE SAATH GENERATOR
# ==========================================
# example.
def mangesh():
    yield 1
    yield 2
    yield 3
for i in mangesh():
    print(i)

# Notice karo
# hamne next() nahi likha 
# loop kud next() call karta hai.


# ==========================================
# RANGE GENERATOR
# ==========================================
# example.
def count():
    for i in range(1,6):
        yield i
for num in count():
     print(num)
# // Output ???


# ==========================================
# GENERATOR MEOMARY KYU BACHAATA HAI ??
# ==========================================
# Normal list
# --> numbers = [1,2,3,4,5,6,7,8,9]
# saari values ek saath memory mein.

# Generator:
# yild -> ek value.
# use ho gayi
# agli value -> use ho gayi
# agli value -> use ho gayi

# islye generator memory efficient hota hai.


# ==========================================
# REAL LIFE USE
# ==========================================
# Generatoe use hota hai.
# - Large files read karne mein
# - Data streaming
# - API's
# - Machine learning
# - Huge database records
# - memory efficient programming


# ==========================================
# GENERATOR VS ITERATOR
# ==========================================
# ITERATOR ===>     
# iter() se banta hai
# iterator manually banana padta hai
# next() use hota hai
# thoda lengthy code
# one by one values dta hai 

# GENERATOR ===>
# yield se banta hai
# python khud generator object bana deta hai
# next() use hota hai
# kam code,easy to write
# one by one values deta hai 


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
def demo():
    yield 5
g = demo()
print(next(g))

# 2)
def number():
    yield 10
    yield 20
g = number()
print(next(g))
print(next(g))

# 3)
def data():
    yield "Python"
for i in data():
    print(i)

# 4)
def test():
    return 10
print(test())

# 5) Generator function mein konsa keyword use hota hai??
# --> yiled => keyword use hota hai


# ==========================================
# MINI PROJECT
# ==========================================
def even_numbers():
    for i in range(2,11,2):
        yield i
for num in even_numbers():
    print(num)
# // Output ???


# To fianlly aaj ka hamar day 30 generator khatam , bass itna he tha
# aur aasan bhi , bahii aise he hota hai python,python ke bas ham concept 
# samja sakte hai pr code to tujhe he likhna padega na khud se 
# kuch nahi bhai assan hai , bass daily consistency se karte ja 
# ho jayega , utna bhi mushkil nahi hai
# to chalo milte hamar agle lecture main kisi new topic ke saath 
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳