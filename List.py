# ==========================================
#              DAY 9 List
# ==========================================

# to kya haal chaal bhai log aagye firse day 9 maine
# to aaj ham padne ja rahe hain list kya hoti hai , to ham aaj list ko detail maine padenge
# kya hota hain kya use case hai aur ise ham kaise banaye okay
# to shurur karte hain bina kisi timepass kiye , dhyaa de


# ==========================================
# LIST
# ==========================================

# LIST --> ek collection hota hain jise ham ek variable maine store karte hain ,
# example ke saath samja ta hu

# soch agar tuze 5 logo ka naam varible maine store karna hain to kya karega

student1 = "sumit"
student2 = "sahil"
student3 = "saurabh"
student4 = "satyam"
student5 = "shubham"

# ab to aise to nahi karega na ,
# soch agar 5 ke jagaha 1000 logo ka naam store karna hain to kya karega ,
# to iske liye ham list ka use karte hain

# kuch aise

students = ["sumit", "sahil", "saurabh", "satyam", "shubham"]

# ab ye sab ek list maine save hain jis list ka naam students hain ,
# to ab tu easily 1000 logo ka naam store kar sakta hain
# aur ise access kar sakta hain ,
# to chal ab aage badte hain.


# ==========================================
# LIST MAINE KYA KYA STORE KAR SAKTE HAIN
# ==========================================

# string, integer, float, boolean , list , tuple ,
# dictionary , set , complex number , etc sab store kar sakte hain.

# aur haan mix data bhi save kar sakte hain

# example.

mix_data = [
    "sumit",
    25,
    5.9,
    True,
    [1, 2, 3],
    (1, 2, 3),
    {"name": "sumit"},
    {1, 2, 3},
    1 + 2j
]


# ==========================================
# LIST INDEXING
# ==========================================

# LIST INDEXING -->
# list maine jo bhi data store karte hain uska ek index hota hain ,
# jisse ham easily access kar sakte hain ,
# to chal ab ise samja ta hu.

# python ise kuch is taraha se dekhta hain

# fruits = ["Apple", "Mango", "Banana"]

# Apple    Mango    Banana
#  0        1         2


# example.

fruits = ["Apple", "Mango", "Banana"]
print(fruits[0])  # // Output ???

fruits = ["Apple", "Mango", "Banana"]
print(fruits[1])  # // Output ???

fruits = ["Apple", "Mango", "Banana"]
print(fruits[2])  # // Output ???


# ==========================================
# NEGATIVE INDEXING
# ==========================================

# ismaine bhi negative indexing hoti hain

# example.

fruits = ["Apple", "Mango", "Banana"]
print(fruits[-2])  # // Output ???

fruits = ["Apple", "Mango", "Banana"]
print(fruits[-1])  # // Output ???


# ==========================================
# LIST KI LENGTH
# ==========================================

# list maine hamne kitni values add ke hai hain uska length nikalne ke liye
# ham len() function ka use karte hain ,
# to chal ise samja ta hu.

fruits = ["Apple", "Mango", "Banana"]
print(len(fruits))  # // Output ???


# ==========================================
# CHANGES IN LIST
# ==========================================

# ise tum kuch ise tara se samjo
# tume ek code kiya hai 1000 - 2000 lines ka
# aur ab tumhe list maine kuch replace karna ,
# kuch add karna ho ya lasta vaala remove karna hain

# ya kisi specific palce pr kisi specific cheej ko add karna ho to ,
# tum pure code maine list to nahi dhund te baithoge na ,
# aur fir use thodi edit karoge

# to waise nahi hota uske liye kuch hota hai
# to ham wo padne ja rahe hai

# aur haa dhyaan se sun meri batt
# eksi koi theory nahi hote
# isee hame example ke saath he samjna hot hai okay

# to chal ab shuru kart hain


# ==========================================
# 1) REPLACE
# ==========================================

# socho mujhe mango ko keplace karna hain orange ke saath
# to kiase karna haine ??

# example.

fruits = ["Apple", "Mango", "Banana"]
fruits[1] = "Orange"

print(fruits)  # // Output ???


# ==========================================
# 2) APPEND()
# ==========================================

# list ke end main value add karta hai

# example.

fruits = ["Apple", "Mango"]

fruits.append("Banana")

print(fruits)  # // Output ???


# ==========================================
# 3) INSERT()
# ==========================================

# kisi specific jagag pe value add kar sakte hain

# example.

fruits = ["Apple", "Banana"]

fruits.insert(1, "Mango")

print(fruits)  # // Output ???


# ==========================================
# 4) REMOVE()
# ==========================================

# value ko remove kar sakte hain

# example.

fruits = ["Apple", "Mango", "Banana"]

fruits.remove("Mango")

print(fruits)  # // Output ???


# ==========================================
# 5) POP()
# ==========================================

# ismain bhai element ko remove kar sakt hain
# par last vaala

# example.

fruits = ["Apple", "Mango", "Banana"]

fruits.pop()

print(fruits)  # // Output ???


# ==========================================
# 6) LIST SLICING
# ==========================================

# list ko beech main se kaat ne main help karta hain ,
# starting se bhi aur last se bhi kaat sakte hain

# example.

numbers = [10, 20, 30, 40, 50]

print(numbers[:4])  # // Output ???


# ==========================================
# 7) CHECK VALUE EXIST OR NOT
# ==========================================

# bass check karta hain tumne value add ke haain ya nahi

# agar hain to true

# nahi to false output

# example.

fruits = ["Apple", "Mango", "Banana"]

print("Mango" in fruits)  # // Output ???

fruits = ["Apple", "Mango", "Banana"]

print("sumit" in fruits)  # // Output ???


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1)

numbers = [10, 20, 30, 40]

print(numbers[0])  # // Output ???


# 2)

fruits = ["Apple", "Mango", "Banana"]

print(fruits[-1])  # // Output ???


# 3)

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)  # // Output ???


# 4)

fruits = ["Apple", "Mango", "Banana"]

fruits.remove("Mango")

print(fruits)  # // Output ???


# 5)

numbers = [10, 20, 30, 40, 50]

print(len(numbers))  # // Output ???


# ==========================================
# END OF DAY 9
# ==========================================

# to aaj hamar day 9 bhi finally khatahm

# to aaj hamne seekha haine list kya hota haine detail maine

# milte hain day 10 maine new topic ke saath

# tab tak ke liye

# JAI HIND
# JAI BHARAT


# List ek collection hai jisme hum multiple values ko ek hi variable mein
# store kar sakte hain aur baad mein unhe modify bhi kar sakte hain.