# ==========================================
#              DAY 16 FUNCTIONS
# ==========================================

# to welcom back , aaj hai day 16 to hamara aaj ka topic hain functions , to aaj ham ise detail mai samjte hai kya hota hain functions .
# Aurr haa ye python ka bohat important topic hain .

# soch tera code 1000-2000 lines ka hai , aur ek hi kaam baar baar karna pad gaya to ?? 
# to kya tu code ko 10 baar likhega kyaa ? nahi na waise nahi hota .
# isi problem ko solve karne ke liye ham function ka use karte hai.
# chal ab detail mai samjte hai kya hota hai , bina kisi timepass kiye samjte hai.

# FUNCTIONS --> aise code ek baar likho , aur jab chahe tab use karo baar baar use karo .
# example.
# soch tere ghar pe washing machin hai , kapde kitni bahi ho , machin ek he kaam karta hain kapde dhona ,
# bass button dabao aur kaam hogaya.
# bass waise he function hote hai ek baar bana lo baad main baar baar call karo .

# ==========================================
# FUNCTION BANATE KAISE HAI ??
# ==========================================
# python main function ko banane ke liye "def" ka use hota hai.
# example se samaj.
def sumit():
    print("hello mangesh")

# abhi run karoge to kuch nahi hoga dekh lo run karke , kyu ki code to hamne kiya pr , jaise hamne padha tha , 
# code ko call to karna padega na 

def sumit():
    print("hello mangesh")
sumit()

# ab run karke dekh run hoga kyu ki hamne , bad main call kiya hain " sumit() " ye call function hai

# ham ek function ko multiple times call kar sakte hain matlab baar baar call kar sakte hain jaise hamne padha tha.
def sumit():
    print("Good morning")
sumit()
sumit()
sumit()
sumit()
# multiple time call kar sakte hain , okay samjha 
# ab tu ye mat soch maine ya pe sumit kyu liya , bhaii variable hai tu kuch bhi le sakta hain , bass call karne
# ke liye use karna padta hai


# ==========================================
# FUNCTION KE ANDAR MULTIPLE STATEMENTS
# ==========================================
def sumit():
    print("My name is SUMIT")
    print("I'am 20 year old")
    print("Day 16 of learning FUNCTIONS")

sumit()

# iis function ke andar hamne multiple statement ka use kiya hai.

# ==========================================
# FUNCTION WITH PARAMETER 
# ==========================================
# ab maan lo tumne code kiya hai, pr tume har baar kuch alag alag print karna ho to kaise karoge ,
# iske liye ham function parameter ka use karta hai
# example.
def sumit(num):
    print("My number : ",num)
sumit(25)
sumit(1)
sumit(2008)
sumit(2007)

# abhi hamne yaha pe kya kiya hai , hame jabhi bhi call karna tha tab hamne alag alag data insert kiya hai aur call kiya ,
# bass ham fuction ko alag alag data bhej sakte hai , jase hame code main jarurat ho tab

# parameter kay hai ??
# sumit(num) sumit(variable) ke andar jo num(paremeter) hai use ham parameter bolte hai.

# ==========================================
# MULTIPLE PARAMETERS IN FUNCTIONS
# ==========================================
# parameter ka matlab to pata hain na , to ab multiple parameter ka use karenge .
# example.
def sumit(name,age,):
    print(name)
    print(age)
sumit("mangesh", 20)
sumit("kalpesh", 21)
sumit("Atkari", 20)

# ismain hamne multiple paramater ka use kiya aur alag alag data daal ke function ko call karke dekho ,
# multiple calls + multiple parameter 


# ==========================================
# RETURN 
# ==========================================
# ab dhya se dekh ye thoda important topic hai
# abhi tak function sirf print kar rahe the .
# par agar function koi value wapas bheje to ??
# uske liye return ka use karte hai
# samja ta hu example se 
# example.
def calci():
    return 10 + 20
sumit = calci()
print(sumit)


# example . use kya hai
def square(num):
    return num * num
b = square(7)
print(b)

# mujhe pata hai kuch bhi nahi samja hoga tuze , chal ab tuje acche se samjata hu 
# Step 1
# b = square(7)
# yaha hamne function ko call kiya aur uske andar value 7 bheji.

# pytho ne num = 7 maan liya . okay yaha tak claer hai na 
# matlab parameter = 7 hai ab.

# Step 2 
# function ke andar ye code hai
# return num * num 
# ab answer 49 milega 

# Step 3 
# ab function ke pass answer hai 49 
# matlab return 49 

# mere kaam ho gaya , ye raha answer 49 ,maine ise wapas(return) us jagah bhej raha hu jahan se mujhe call kiya gaya tha .
# matlab return karega answer ko.

# Step 4 
# hamne function ko kuch aise call kiya tha 
# b = square(7)
# function ne 49 answer bheja 
# python to hai he padhalikha usne automatically 
# b = 49 kar diya 
# ab variable(b) = 49
# to output 49 aayega 

# Argument function ke andar jata hai → Function processing karta hai → Return result wapas bhejta hai → Hum us result ko variable mein store ya print kar sakte hain. 


# ==========================================
# FUNCTION + USER INPUT 
# ==========================================
# kuch nahi karna user input add karna hai jaise ham abhi tak karte ja rahe hai
# example.
def xyz(name):
    print("welcom" , name)
name = input("Enter name : ",)
xyz(name)


# ==========================================
#  FUNCTION KA FLOW
# ==========================================
# example.
def hello():
    print("Hello")

print("Start")

hello()

print("End")


# python upar se nich padta hai , ab yaha pe kya hoga 
# // Output ???
# start
# Hello
# End
# 
# Aise kyu hua ??
# kyu ki hamne print("Hello")
# likha fir, lekin tum khud dekho isme print pe nahi chlta hai function ko call karna padta hai 
# hamne baad main call kiya , Print("Start") ke baad 
# aur Print("Start") is liye pehle print hua kyi ki ye function ke bahar hai 
# indentation nahi hai 
# aur last main End 


# PRACTICE QUESTION 

# 1)
def greet():
    print("Hello")
greet()

# 2)
def show():
    print("Python")
show()
show()

# 3)
def square(num):
    return num * num
answer = square(5)
print(answer)

# 4)
def add():
    return 5 + 10
print(add())

# 5)
def intro(name):
    print("Welcome", name)
intro("Sumit")


# MINI PROJECT
def student(name, age):
    print("Name :", name)
    print("Age :", age)

name = input("Enter Name : ")
age = int(input("Enter Age : "))

student(name, age)

# To finally aaj hamar day 16 khatam to aaj hamne function ko samj liye , aur prctice kar taaki tuze aurr achhe se samj mai aaye 
# FUNCTION bahi mai personally ise code mai use karna pasand karta hu taaki time bach sake aurr code jayda lamba na bane 
# ye topic importanat hai aage jake DSA , Project , Advance python sab jagah use hoga 
# to ise acche se practice kar 

# to mailte hai day 17 main new topic ke saath 
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
