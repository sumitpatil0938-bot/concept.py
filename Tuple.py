# ==========================================
#             DAY 10 TUPLE
# ==========================================

# to aaj hain day 10 jis main ham padhne ja rahe hain tuple ko ,
# jaise hamne day 9 main padha list kya hoti hain use case aur uske problems bhi solve kiye
# to aaj ham usi taraha tuple ko samjne vaale hain starting to end tak
# to shuru karte hain binka kisi time pass kiye


# ==========================================
# TUPLE
# ==========================================

# TUPLE --> iska matlab ek variable ke andar ham multiple values stor kr sakte hain ,
# bass kuch nahi same to same list ke jaise he hai .

# list --> square brackat "[ ]"
# tuple --> round brackrt "( )"

# example ke saath samjte hain

# list
fruits = ["Apple", "Mango", "Banana"]

# tuple
fruits = ("Apple", "Mango", "Banana")


# ==========================================
# IMMUTABLE
# ==========================================

# IMP --> tuple immutable hota hain , batata hu batata hu
# iska matlab hmm ise change nahi kar sakte ek barr bana diya to bana diya .

# example.

fruits = ("Apple", "Mango", "Banana")
fruits[1] = "Orange"

print(fruits)  # // Output ???

# output maine error aayega kyu ki bracket ke andar ke values change ya replace nahi kar sakte

# list maine jaise hamne dekha tha ham alag alag typecasting use karke
# list ke andar chnages kar rahe the pr tuple ke andar nahi kar sakte

# example ke saath samjlo

# soocho agar hame aise list banani ho jise koi chnage nhai kar sake
# to hame tuple ka use karna padega ,
# list to chnage ho sakte hain to ham usse use maine nahi le sakte .

days = ("Mon", "Tue", "Wed", "Thu", "Fri")
months = ("jan", "feb", "mar", "apr", "may")

# ye jo values hain ham barr barr change nahi karte


# ==========================================
# MAKING OF TUPLE
# ==========================================

# what if there is single value in tuple

num = (3)

# abe to ye tuple nahi integer ban jayega , haa

# tuple ko likhne ke liye uske andar comma laga na padega
# tabhi jake wo tuple banega

num = (3,)

# ab ye tuple ban gaya

# aur multiple values hogi to ,
# normal jaise bana te haine bass waise he

numbers = (10, 20, 30, 40)


# ==========================================
# TUPLE CAN STORE ??
# ==========================================

# ye bhi list ke jaise he hota hain ,
# ismain bhi ham kuch bhi add kar sakte hain tuje jo add karna hain wo add kar de tu,

# string, integer , float , dictionary , boolean , set ,
# complex number , list , tuple ,
# haa tujhe jo kuch store karna hai karle

# bass yadd rak baad maine change nahi kar sakte

data = (
    "sumit",
    9,
    5.9,
    {"name : sumit "},
    (1, 2, 3),
    [4, 5, 6],
    True,
    False
)


# ==========================================
# TUPLE INDEXING
# ==========================================

# dekha bhai ise maine fir se explaine karke timepass nahi karung
# same to same hai bahi jaise hamne list maine padha tha


# ==========================================
# 1) INDEXING
# ==========================================

# example ke saath samaj ja

fruits = ("Apple", "Mango", "Banana")

# Apple   Mango   Banana
#  0       1       2


# 1)

fruits = ("Apple", "Mango", "Banana")
print(fruits[0])  # // Output ???


# 2)

fruits = ("Apple", "Mango", "Banana")
print(fruits[2])  # // Output ???


# ==========================================
# 2) NEGATIVE INDEXING
# ==========================================

# example ke saath samaj ja

fruits = ("Apple", "Mango", "Banana")

# Apple   Mango   Banana
# -3      -2      -1


# 1)

fruits = ("Apple", "Mango", "Banana")
print(fruits[-1])  # // Output ???


# 2)

fruits = ("Apple", "Mango", "Banana")
print(fruits[-3])  # // Output ???


# ==========================================
# TUPLE LENGTH
# ==========================================

# tuple maine kitni value hai pata karne ke kiye use hota hai tuple length

# example.

fruits = ("Apple", "Mango", "Banana")
print(len(fruits))  # // Output ???


# ==========================================
# TUPLE SLICING
# ==========================================

# iska use ham tuple ko cut karne ke liye use karte hain aur ha
# ye bhi same to same lis ke jaise he hain ,
# jaise list slicing this bass same to same

# example


# 1)

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # // Output ???


# 2)

numbers = (10, 20, 30, 40, 50)
print(numbers[:4])  # // Output ???


# 3)

numbers = (10, 20, 30, 40, 50)
print(numbers[3:])  # // Output ???


# ==========================================
# CHECK VALUE EXIST OR NOT
# ==========================================

# hamare 1000-2000 line ke code ke andar jo tuple hota hain uske andar ke values ko check karta hain 

# example.


# 1)

fruits = ("Apple", "Mango", "Banana")
print("Mango" in fruits)  # // Output ???


# 2)

fruits = ("Apple", "Mango", "Banana")
print("sumit" in fruits)  # // Output ???


# ==========================================
# LOOP THROUG TUPLE
# ==========================================

# ye jo loop ka concept hai wo DSA ka part hain matlab python main he
# DSA(data structure and algorithm),
# to ye tuhme samaj maine nahi aayega ye ham next series maine shuru karenge

# ye khatam hone ke daab ,
# to bass abhi ke liye kuch mat kar bass dekha

# maine kaise code kiya hai samjne ke koshish mat kr

# example.

fruits = ("Apple", "Mango", "Banana")

for fruit in fruits:
    print(fruit)  # // Output ???

# bass ise print karke dekh le


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1)

numbers = (10, 20, 30)
print(numbers[1])  # // Output ???


# 2)

fruits = ("Apple", "Mango", "Banana")
print(fruits[-1])  # // Output ???


# 3)

numbers = (10, 20, 30, 40)
print(len(numbers))  # // Output ???


# 4)

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # // Output ???


# 5)

fruits = ("Apple", "Mango", "Banana")
print("Orange" in fruits)  # // Output ???


# ==========================================
# MINI PROJECT
# ==========================================

name = input("Enter Name : ")
age = int(input("Enter Age : "))

details = (name, age)

print(details)  # // Output ???


# ==========================================
# END OF DAY 10
# ==========================================

# to finally day 10 khatam to aaj hamne padha tuple ke baare main

# to bhaii isme jayad demak lagne ke koi jarurat to nahi thi na ?? ,
# aree assan hai bhaii bolat tha na bass daily ke daily karte ja

# breka mat liye kar waise bhi 15-20 min to lagte honge na karne maine
# to karte ja

# bass aise he bich maine eassy hard topic aate jate hain
# to tension mat liye kar

# to milte hain day 11 main tab tak ke liye

# jai hind
# jai bharat