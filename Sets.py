# ==========================================
#              DAY 11 SETS
# ==========================================

# firse swagat karta hu day 11 , to aaj hamara topic hain sets ,
# aaj ham sets ko detail main samjte hain time pass nahi karte kyu ki ye bhi chota he topic hain utna bada nahi hai 
# aur easy bhi hai 
# to bina time pass kiye shuru karte hain day 11 sets 

# ==========================================
# SETS
# ==========================================

# SETS --> ye bhi list , tuple ke jaise he hain , multiple values store karta hai ,
# aur ise ham curly bracket " { } " se indicate karte hain .

# LIST --> SQUARE BRACKET []
# TUPLE --> ROUND BRACKET ()
# SETS --> CURLY BRACKET {}

# example.
fruits = {"Apple", "Mango", "Banana"}
print(fruits) # // Output ???


# ==========================================
# SPECIAL PROPERTIES
# ==========================================

# 3 important properties hain 

# 1) Duplicate vaues allow nahi karta hain , matlab ??
# agar kisi set maine ek he value dobara aagyi to use allow nahi karta ,
# use run karne ke badd use bass ek he bar show karta hain.

# example.
fruits = {"Apple", "Mango", "Apple", "Banana"}
print(fruits) # // Output ???

# isme apple 2 times aaya hain to use python ek he barr print karega , abhi samja .


# 2) Unordered hota hain , matlab ???
# matlab , isme indexing nahi hoti ,
# jaise ham log list , tuple maine karte the ,
# set indexing ko allow nahi karta ,
# iska matlab ham ismin set ke slicing nahi kar sakte ,
# haa nahi kar sakte ham slicing

# example .
fruits = {"Apple", "Mango", "Banana"}
print(fruits[2]) # // Output ???

# is code main error aayega kyu ki indexing nahi hote hai na 


# 3) Mutable hota hain
# jaise hamne padha tha list (mutable) , tuple (immutable) , sets (mutable)
# sets mutable hain ,
# iska matlab ham set ke andar ham values add aur remove kar sakte hain ,
# pr ismai indexing nahi hota hai to ham kisi specific palce pr kuch add nahi kr sakte.

# example
fruits = {"Apple", "Mango", "Banana"}
fruits.insert(2,"banana")
print(fruits) # // Output ???

# erroe aayega allow nahi karta


# ==========================================
# SET KAISE BANATE HAIN
# ==========================================

# curly bracket ke andar jo bhi data daaloge usee python set samjte hain

# example.
numbers = {10, "sumit", 3.56, 4 + 3j}
print(numbers) # // Output ???


# ==========================================
# EMPTY SET
# ==========================================

sumit = { }

# python ise empty set nahi dictionary maanta hai
# kyu ki dictionary bhi curlya bracket maine he hoti hain

sumit = set()
print(sumit) # // Output ???

# ab tumhe ek question aayega , set to curly bracket main hota hain
# to hamne ise round bracket main kyu likha
# tu bass etna yadd rakh empty set kaise likha jate hain
# aur round bracket use hota hain , dhyaa rakh bass


# ==========================================
# STORAGE OF SET
# ==========================================

# ye bhi list,tuple ke taraha hai samte to same
# ism min ham kuch bhi add kar sakte hain
# string , integer , float , list , tuple , dictionary ,
# complex numbers, stes and etc add kar sakte hain

# example.
sumit = { "mangesh",25,1.6,[1,2,3],(4,5,6),{"name : sumit"},2 - 5j,{"ved",2,7}}
print(sumit) # // Output ???


# ==========================================
# ADD IN SETS
# ==========================================

# set main ham value to add karte hain
# pr wo value bich main nahi add hoti
# wo value last main add hoti hai ,
# bich main add karne ke liye indexing allow honi chaiye ,
# isme indexing nahi hoti

# example.
fruits = {"Apple", "Mango"}
fruits.add("Banana")
print(fruits)  # // Output ???


# ==========================================
# REMOVE IN SETS
# ==========================================

# set main ham value remove karte hain

# example.
fruits = {"Apple", "Mango", "Banana"}
fruits.remove("Mango")
print(fruits) # // Output ???


# ==========================================
# POP() IN SETS
# ==========================================

# ye jo pop() hain wo random value remove karta hain set main se ,
# konsi bhi value ho sakte hain

fruits = {"Apple", "Mango", "Banana"}
fruits.pop()
print(fruits) # // Output ???


# ==========================================
# LENGTH OF SETS
# ==========================================

# ye batata hai ke set ke length ketni badi hain

# example.
fruits = {"Apple", "Mango", "Banana"}
print(len(fruits)) # // Output ???


# ==========================================
# VALUE CHECKING IN SET
# ==========================================

# ye bass check karta hain hamare 1000 - 2000 line ke code main
# hamne kahi to set ka use kiya hoga
# to hamne us set mai kya add kiya hai ya kya nahi
# ye dekhne ke liye use hota hai

# iska out put true ya false mai atta hain

# example.
fruits = {"Apple", "Mango", "Banana"}
print("Mango" in fruits) # // Output ???

fruits = {"Apple", "Mango", "Banana"}
print("Sumit" in fruits) # // Output ???


# ==========================================
# CLEAR()
# ==========================================

# yr jo typecasting hain iska use set ko pura clear karne main help karta hain ,
# matlab set empty ho jata hain ye function use karne se

# example .
fruits = {"Apple", "Mango", "Banana"}
fruits.clear()
print(fruits) # // Output ???


# ==========================================
# LOOP IN SET
# ==========================================

# ye dsa ka part hai jaise hamne kal tuple mein padha tha ,
# iske help se hamar jo set hain wo ek loop main aaja ta hain

# matlab set ke andar ka data , ek line main aata hain aur
# python set ke andar ke data ke pass ek - ek karke visit karta hain
# aur use print kart hai

# example .
fruits = {"Apple", "Mango", "Banana"}

for fruit in fruits:
    print(fruit) # // Output ???

    # tumhe kuch samaj nahi ayyega bass program run karke dekho , okay


# ==========================================
# PRACTICE PROBLEM
# ==========================================

# 1)
numbers = {10, 20, 30}
print(len(numbers))

# 2)
fruits = {"Apple", "Mango"}
fruits.add("Banana")
print(fruits)

# 3)
fruits = {"Apple", "Mango", "Banana"}
fruits.remove("Mango")
print(fruits)

# 4)
fruits = {"Apple", "Mango", "Banana"}
print("Apple" in fruits)

# 5)
numbers = {10, 20, 30, 10}
print(numbers)


# ==========================================
# PROJECT
# ==========================================

names = set()

name1 = input("Enter Name : ")
name2 = input("Enter Name : ")
name3 = input("Enter Name : ")

names.add(name1)
names.add(name2)
names.add(name3)

print(names)


# ==========================================
# END OF DAY 11
# ==========================================

# to finally aaj hamar day 11 khatam sets ke saath ,
# easy tha bohat easy tha ,
# to ab milte hamare kal ke lecture main

# day 12 maine tab tak ke liye

# jai hind
# jai bharat