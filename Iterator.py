# ==========================================
#              DAY 29 ITERATOR
# ==========================================
# to kya haal chal bahi log , welcome back to day 29
# to aaj ka hamar topic hai iterator ,
# bahii sach main bata raha hu aaj ka topic bohat aasan hai
# to shuru karte hai bina kisi timepass kiye 
# agar iterator samaj gaya to baad main generator bhi aasan lagenge


# ==========================================
# ITERATOR KYA HOTA HAI ?
# ==========================================
# --> iterator ek object hai jo collection(list,tuple,string,set,etc.)ki value ek-ek karke return
#     karta hai
# matlab saari values ek saath nahi deta
# ek baar main sirf ek value deta hai.
# example.
# Soch tere pass ek book hai
# book main 500 pages hain.
# kya tu saare pages ek saath padh leta hai?
# nahi na 
# pehle page 1 -> page 2 -> page 3 -> page 4
# isi tarah iterator bhi values ko one by one retue=rn karta hai.


# iterable padhne se pehle ek aur word samajh.
# iterable matlab wo object jiske upar iterate(loop) kar sakte hai.
# example.
# list , tuplr , set , string , dictionary
# yeh sab iterable hai.
# example.
# list => numbers = [10,20,30]
# list hai.
# iske upar loop chalta hai.
# isliye ye iterable hai.


# ==========================================
# ITERABLE KAISE BANATE HAI ??
# ==========================================
# python main: iter()
# function use hota hai.
# example.
numbers = [10,20,30]
sumit = iter(numbers)
print(sumit)
# // Output ???
# ab jo output aaya na wo alag alag device ke liye alag alag aata hai.


# ==========================================
# NEXT()
# ==========================================
# iterator ki next value lene ke liye
# next()
# use karte hai.
# example.
numbers = [10,20,30,40]
sumit = iter(numbers)
print(next(sumit))
# // Output ???
# check kar lena 
# Agara aage vaala number chaiye to ek aur baar print ka use karna padega,
# example.
numbers = [1,2,3,4]
sumit = iter(numbers)
print(next(sumit))
print(next(sumit))
# fir aur ek baar print kar aur 3rd value mil jayege
# bass itna he hai iterator.

# Step by Step
# number = [5,6,7,8,9] = list bani.

# sumit = iter(number) = iterator bana.

# print(next(sumit)) = pehli vale di.
# print(next(sumit)) = dusri vale di.
# print(next(sumit)) = teesri vale di.


# agar sari value khatam ho gayi to
# example.
numbers = [1,2]
mangesh = iter(numbers)
print(next(mangesh))
print(next(mangesh))
print(next(mangesh))
# // Output ???
# kyu?? , kyuki iterator ke pass aur koi value nahi hai.
# saari values khatam


# ==========================================
# LOOP AUR ITERATOR
# ==========================================
# tum soch te hoge 
# for
# loop kaise chalta hai?
# bahi uske andar(internally) bhi python ye same code ka use karta hai 
# example.
numbers = [4,5,6]
for i in numbers:
    print(i)
# python internally same he code run karta hai 
# code --> it = iter(it)
#          print(next(it))
#          print(next(it))
#          print(next(it))


# ==========================================
# STRING ITERATOR
# ==========================================
# iterator sirf list ke liye nahi.
# string ke liye bhi work karta hai.
# example.
name = "Sumit"
aa = iter(name)
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
# // Output ???


# ==========================================
# TUPLE ITERATOR
# ==========================================
# same bahi ise tuple main bhi use kar sakte hai.
# example.
data = (100,200,300,400)
ss = iter(data)
print(next(ss))
print(next(ss))
print(next(ss))
# // Output ???


# ==========================================
# ITERATOR KO TOD KAR SAMJHO
# ==========================================
# collect -> iterator -> next() -> one value -> next() -> next vale -> next() -> next value -> 
# stopeiterator at the end of collection


# ==========================================
# ITERATOR KA USE KYA HAI ?
# ==========================================
# iterator ka use hota hai
# -> Large data read karne mein
# -> File handling
# -> Database records
# -> Generator
# -> memory efficient programming

# kyuki ye ek baar mein sirf ek value memory mein rakhta hai.


# ==========================================
# LET'S PRACTICE 
# ==========================================
# 1)
numbers = [1,2,3]
it = iter(numbers)
print(next(it))

# 2)
numbers = [10,20]
it = iter(numbers)
print(next(it))
print(next(it))

# 3)
name = "Python"
it = iter(name)
print(next(it))

# 4)
data = (100,200)
it = iter(data)
print(next(it))

# 5)
numbers = [1]
it = iter(numbers)
print(next(it))
print(next(it))


# ==========================================
# MINI PROJECT
# ==========================================
fruits = ["Apple","Mango","Banana","Pineapple"]
aavi = iter(fruits)
print(next(aavi))
print(next(aavi))
print(next(aavi))
print(next(aavi))


# Iterator = Object jo collection ki values ek-ek karke return karta hai.
# iter(collection)
# next(iterator)

# to bahii finally aaj hamar day 29 kahatam ab tak ke sabse hard topic ke saath
# majak bhi log , to hamne iterator ko aaj detail main samja,
# bass itne he hai iterator.
# to milte hai hamare next lecture main day 30 main kisi new topic ke saath
# tab tak liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳