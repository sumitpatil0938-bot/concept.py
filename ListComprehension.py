# ==========================================
#          DAY 22 LIST COMPREHENSION
# ==========================================

# to kay haal chaal bahi log welcome back to day 22 , 
# to aaj ka hamara topic hain ListComprehension , assan hai bass iska naam bada hai 
# topic to bohat easy hai,
# to chalo shurvat karte hain bina kisi time pass kiya 

# to bhai aaj ham day 9(List) + day 14(Loops) co merge karke code karne vaali hai
# dekh abb kaise samju tuze , python ham log padha sakte hain 
# pr code to tuze he likhna padega khud se okay
# aurr tuze hi samjna hoga kaise kiya kyu kiya , logic samja har code ke 


# ==========================================
# LIST COMPREHENSION
# ==========================================
# --> list bana ne ka shortcut hai
# abhi tak ham aise list bana rahe the 
numbers = []
for i in range(1,6): # Day 14
    numbers.append(i) # Day 9
print(numbers) 

# ye sahi method hai pr
# python bolta hai bhai log agar code ka logic small hai to
# tu itna bada code mat likha kr
# iske liye ham shortcut ka use karte hai usee he ham (List Comprehension) bolte hai

# abhi jo hamne upar likha wo normal method hai 

# ==========================================
# LIST COMPREHENSION WAY
# ==========================================
# example.
numbers = [i for i in range(1,6)]
print(numbers) # // Output ???

# ye shortcut method hai use karne ka 
# tu khud dekh le code main difference 
# aur dono ka output same he aayega 

# Syntax : [ expression for item in iterable]
# example.
sumit = [i for i in range(1,11)]
print(sumit) # // Output ???

# i = value hai 
# for i in range(1,11) = loop hai.
# python har value ko list mein daal raha hai for i in range ke help se.


# ==========================================
# SQUARE NUMBER LIST
# ==========================================
# exmaple.
square = [i * i for i in range(1,6)]
print(square) # // Output ???


# ==========================================
# STRING LIST
# ==========================================
# example.
name = ["sumit","mangesh","sahil"]
upper_name = [name.upper() for name in name]
print(upper_name) # // Output ???


# ==========================================
# IF CONDITION IN LIST COMPREHENSION
# ==========================================
# sirf even number lo
# normal example.
even = [ ]
for i in range(1,11):
    if i % 2 == 0:
        even.append(i)
print(even) # // Output ???

# list comprehension example.
even = [i for i in range(1,11) if i % 2 == 0]
print(even) # // Output ???

# aise he odd numbers ka try karke dekho khud se.


# ==========================================
# LENGTH OF WORDS
# ==========================================
# example.
name = ["sumit","sahil","avishkar","mangesh"]
length = [len(name) for name in name]
print(length) # // Output ???


# ==========================================
# LIST COMPREHENSION KO TOD KAR SAMJTE HAI 
# ==========================================
# example.
numbers = [i * 2 for i in range(5)]
# --> python ise internally kuch aise samajhta hai
numbers = [ ]
for i in range(5):
    numbers.append(1*2)

# OUTPUT --> [0,2,4,6,8]

# bas mere bhaii pura logic hai ye.
# aur kuch nahi hai ismai.


# ==========================================
# KAB USE KARNA HAI 
# ==========================================
# 1) New list banani ho.
# 2) Loop chalana ho. 
# 3) Data modify karna ho. 
# 4) Code short likhna ho. 


# ==========================================
# KAB USE NAHI KARNA 
# ==========================================
# 1) agar logic bada ho 10-20 line ka code to usse use nahi karte 
#    bass choti choti baato ke liye karte hai.
# 2) agar logic bada ho to normal vaala he use karo.


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
numbers = [i for i in range(1, 6)]
print(numbers) # // Output ???

# 2)
square = [i * i for i in range(1, 5)]
print(square) # // Output ???

# 3)
odd = [i for i in range(1, 11) if i % 2 == 1]
print(odd) # // Output ???

# 4)
names = ["SUMIT", "PRANAV"]
lower = [name.lower() for name in names]
print(lower) # // Output ???

# 5)
numbers = [i * 3 for i in range(1,6)]
print(numbers) # // Output ???


# ==========================================
# MINI PROJECT
# ==========================================
# Q) user se 5 numbers lo aur unka square list comprehension se banao ?
numbers = [ ]
for i in range(5):
    num = int(input("Enter number : "))
    numbers.append(num)
print(numbers)
square = [i * i for i in numbers]
print(square)



# so finally aaj hamara day 22 khatam 
# to bhaii aaj ka topic easy tha , aage bhi aise he topic aane waale hai
# Aur ha ho sake to DSA bhi chalu kar de python main 
# taaki aage aane vaale topic tuze acche se samaj main aaye 
# practice kar aur daily revision karte ja 
# to milte hai day 23 main kisi new topic ke saath tab tak ke liye

# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳


