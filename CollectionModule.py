# ==========================================
#        DAY 35 COLLECTION MODULE
# ==========================================
# to kya haal chal bhi log firse swagat hai day 35 main.
# aaj ham padhne ja rahe hain collection module ke baare main.
# pehli baar naam sunke lag sakta hai ki ye list , tuple aur 
# dictionary ka hi topic hoga.
# lekin aisa nahi hai
# collection module python ka ek specila module hai jo hame
# kuch powerful data structure deta hai.
# inse hamare code aur fast , clean aur easy ho jata hai.
# to bina kisi time pass kiye shuru karte hai.


# ==========================================
# COLLECTION MODULE KYA HOTA HAI ?
# ==========================================
# simple language me.
# collection module python ka built-in module hai.
# ye hamne normal
# - List
# - Tuple
# - Dictionary

# se bhi better aur powerful data structure provide karta hai.
# simple definition yaad rakh.
# Collection Module = Python ka built-in module jo extra data structure provide karta hai.


# ==============================================
# COLLECTION MODULE IMPORT KAISE KARTE HAIN ?
# ==============================================
# example.
# --> import collection

# ya agar sirf ek class use karni ho.
# --> from collection import counter

# ya 
# --> from collection import deque

# ya
# --> from collection import defaultdict


# ==========================================
# COLLECTION MODULE MAIN KYA-KYA HOTA HAI?
# ==========================================
# sabse famous classes.
# 1) Counter
# 2) deque
# 3) defaultdict
# 4) nametuple
# 5) OrderDict
# 6) ChainMap

# Aaj ham in sabka basic concept samjhenge.


# ==========================================
# COUNTER
# ==========================================
# sabse pehle counter.
# Counter ka kaam hota hai.
# kitni baar koi value repeat hui hai uski counting karna.
# example.
from collections import Counter
data = ["apple","banana","apple","mango","apple","banana"]
result = Counter(data)
print(result)
# // Output ???

# YE KAISE CHALA ?
# step by step
# List gayi
# counter ne har item count kiya.
# apple 3
# banana 2
# mango 1
# output mil gaya simple.


# ==========================================
# STRING KE SAATH COUNTER
# ==========================================
# example.
from collections import Counter 
text = "python"
print(Counter(text))
# // Output ???


# ==========================================
# MOST_COMMON()
# ==========================================
# ye sabse jyada repeat hone wali value batata hai.
# example.
from collections import Counter
text = "banana"
c = Counter(text)
print(c.most_common(1))
# // Output ???


# ==========================================
# DEQUE
# ==========================================
# Full form :- Double Ended Queue
# Data ko left aur right dono side se insert aur delete kar sakte hai.

#  NORMAL LIST
# example.
numbers = [10,20,30]
# list me beginning me insert karna slow hota hai.
# isliye deque use karte hai

# DEQUE BANANA
# example.
from collections import deque
d = deque([10,20,30])
print(d)
# // Output ???

# APPEND()
# right side ke end main value add karta hai
# example.
from collections import deque
d = deque([10,20])
d.append(30)
print(d)
# // Output ???

# APPENDLEFT()
# left side value add karta hai.
# example.
from collections import deque
d = deque([20,30])
d.appendleft(10)
print(d)
# // Output ???

# POP()
# Right side se remove karta hai.
# example.
from collections import deque
d = deque([100,200,300])
d.pop()
print(d)
# // Output ???

# POPLEFT()
# left side vaala element remove karta hai.
# example.
from collections import deque
d = deque([5,6,7])
d.popleft()
print(d)
# // Output ???


# ==========================================
# DEFAULTDICT
# ==========================================
# kabhi kabhi dictionary me key nahi hoti
# example.
student = {
    "name" : "simran"
}
print(student["age"])
# // Output ???
# erroe aayega 
# isi problem ko solve karne ke liye 
# ham defaultdict ka use karte hai.
# example.
from collections import defaultdict
student = defaultdict(int)
print(student["age"])
# // Output ???
# error nahi aaya
# kyu ki hamne int ka default value 0 hota hai.


# ==========================================
# NAMEDTUPLE
# ==========================================
# ye tuple ko naam de deta hai.
# example.
from collections import namedtuple
Student = namedtuple("Student",["name","age"])
s = Student("Sumit",20)
print(s.name)
# // Output ???

# NORMAL TUPLE
student = ("sumit",20)
# name print karo
print(student[0])
# index yaad rakhna padta hai.

# namedtuple main
print(s.name)
# ye jyada redable hai.


# ==========================================
# ORDEREDDICT
# ==========================================
# ye dictionary order maintain karta hai.
# python ko naya version me dictionary bhi oredr maintain karti hai.
# lej=kin pehle orderedict bahut use hoti thi.
# example.
from collections import OrderedDict
data = OrderedDict()
data ["A"] = 1
data ["B"] = 2
print(data)
# // Output ???


# ==========================================
# CHAIONMAP
# ==========================================
# ye multiplr dictionaries ko ek sath treat karta hai.
# example.
from collections import ChainMap
d1 = {
    "name" : "mangesh"
}
d2 = {
    "age" : 20
}
data = ChainMap(d1,d2)
print(data["age"])
# // Output ???


# ==========================================
# REAL LIFE USE
# ==========================================
# Collection module ka use hota hai.
# - Data Analysis
# - Machine Learning
# - Cybersecurity
# - Banking Software
# - Search Engines
# - Large Data Processing
# - Web Applictaions


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1)
from collections import Counter
data = [1,2,2,3,3,3]
print(Counter(data))
# // Output ???

# 2)
from collections import deque
d = deque([10,20])
d.appendleft(5)
print(d)
# // Output ???

# 3) Collections Module import karne ke liye kya likhenge ??

# 4) Counter kis kaam ke liye use hota hai ??

# 5) Deque ka full form kya hai ??


# ==========================================
# MINI PROJECT
# ==========================================
from collections import Counter
sentence = input("Enter Sentence : ")
words = sentence.split()
count = Counter(words)
print(count)


# Collections Module = Python ka built-in module jo powerful Data Structures provide karta hai.
# aurr ha bhi log 
# ye classes kabhi mat bhool jana 
# ho sake to rat lo isee acche se
# Counter()
# deque()
# defaultdict()
# namedtuple()
# OrderedDict()
# ChainMap()

# to finally aaj hamara day 35vcomplete hua pehle collections 
# module bada lagega,
# lekin dheere dheere practice karega to ye bohot easy
# lagne lagega.
# sabse important counter aur deque hai.
# to cahlo milte hain day 36bmain kisi new topic ke saath tab tak ke liye.
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳