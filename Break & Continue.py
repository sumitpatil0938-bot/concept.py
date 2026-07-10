# ==========================================
#         DAY 15 BREAK & CONTINUE
# ==========================================

# To kaise ho bhai log , firse swagat hai day 15 main to aaj ka hamar topic hain Break & Continue jise ham loop main use karenge .
# chota aur assan hain bass acche se samaj jana thoda practice bhi kiya kar,
# to chal shuru karte hai bina kisi time pass kiye day 15 ko , aur haa ek barr day 14 ka revision kar lena 5 min main okay.

# Break & Continue --> iska use ham loop ko bich main rokne ke liye hota hai , ya kisi iteration ko skip karne ke liye .
# example ke saath samjte hai 

# ==========================================
# BREAK 
# ==========================================
# --> loop ko turant stop karne ke liye use hota hain .
# matlab jaha pe break statement likh diya loop waha pe he stop hota hai , agar nahi lika to loop continue hota hai last tak.
# example .
for i in range(3,31):
    if i == 25:
        break
    print(i) # // Output ???

# ab tu khud se dekh hamne yaha pe break ka use kiya hai aur hamara loop turant rukh gaya .
# ab samja na pakka , agar ye samj main nahi aaya code kaise kiya to day 14 ko revise kr le okay.

# ab tu dekh 3 se start ho gaya pr jab tak i(25) == 25 matlab condition true nahi hui tab tak run ho raha tha 
# pr jab i(25) == 25 condition true ho gayi to loop ko break statement se ruka diya .

# example.
for i in range(6):
    if i == 4:
        break
    print(i) # // Output ???

# example.
# socho tumhe apne dost ko dhund na hai, aur list me naam diya hai , to iska use karke code likh te hai.
friends = ["sumit","mangesh","sahil","kalpesh","chaitanya","sahivani","pranvi"]

for friend in friends:

    if friend == "kalpesh":
        break
print("mil gaya") # // Output ???

# ab jaise he kalpesh naam mil gaya bass waise he break laga deta hai aur loop ko stop kar deta hain ,
# ab aage vaale naam ko check nahi karega .


# ==========================================
# CONTINUE 
# ==========================================
# --> loop ko stop nahi karta jaise break work karta tha , ye bass current iteration skip karta hai .
# example.
for i in range(7):
    if i == 5:
        continue
    print(i) # // Output ???

# ab tu jab ise run karke dekhega tu khud dekhega , isne "5" ko skip kar diya hai 
# aur baki saare numbers ko print krdiya , jaise he condition true mil gayi " i(5) == 5 " usne 5 ko skip mar diya 


# aur indentation bahi bohat important hota hai , agar tu indentation ko dhya mai nahi rak kar print karega to output alag he aayega , chahe tera code sahi kyu na ho.

# example.
for i in range(1,31):
    if i % 3 == 0:
        continue
    print(i) # // Output ???
# to isme 3 ke table main aane vaale saare numbers ko skip kar diya 
# tum even no ko bhi skip kar sakte ho bass , condition change karte jao jaise tume chaiye okay.
# aage aage to aur intresting hote jata hai topics , tu bass dekhte ja 


# ==========================================
# BREAK VS CONTINUE
# ==========================================
# BREAK --> LOOP KO STOP KARTA HAI , CONDITION TRUE MILNE KE BAAD.
# example.
for i in range(1,21):
    if i == 4:
        break
    print(i) # // Output ???

# CONTINUE --> KISI SPECIFIC ITERATION KO SKIP KARTA HAI ,  CONDITION TRUE MILNE KE BAAD.
# example.
for i in range(1,7):
    if i == 4:
        continue
    print(i) # // Output ???

# difference clear hona chahiye
# break = ruk ja.
# continue = iteration ko skip kar aage badh ja.

# ==========================================
# BREAK IN WHILE LOOP 
# ==========================================
# break ka use while loop min jayda hota hai.
# example.
i = 1
while i <= 10:
    if i == 4:
        break
    print(i) # // Output ???
    i += 1

# i += 1 doubt aaya ya nahi ki hamne aise kyu likha aaya to hoga agar python dhya se padh raha hoga to ,
# to chal isee acche se samja ta hu 
# ise ham while loop mai he use karte hai kyui ki value update karni hoti hai, for loop khud value update karta hai.
# nahi samja hoga samja ta hu 
# ab python ka flow kuch aisa hai 

# step 1
# i = 1
# ab i ki value 1 hai

# step 2
#while i <= 10:
# check karega
# 1 <= 10
# true hai 
# to loop ke andar jayega

# step 3
# if i == 6:
# 1 == 6 
# false 
# ab yaha pe break nahi chalega , kyki break tab lagta hain ja condition true ho ,
# pr ya pe false hai to break nahi lagega to 
# print(i) 
# i = 1

# step 4
# i += 1 
# iska matlab hai 
# i = i + 1 (or) i += 1 
# same hai
# matlab 
# i = 1 + 1
# ab
# 1 = 2
# ho gaya
# fir loop vaapas upar jayega

# Ab fir se check karega 
# 2 <= 10
# true
# print karega 
# 2 
# i += 1
# ab i = 2
# 2 += 1
# i = 3

# aise he chalta rahega 
# jab i == 4
# condition true ho jayege
# ab break lagega , aur loop wahi khatam

# ye jistna mushkil lag raha hai unta hai nahi ye typing ke wajse mushkil lag raha hai 
# agar main bol ke samja tu ho jayega 

# ==========================================
# CONTINUE IN WHILE LOOP 
# ==========================================
# example.
i = 0
while i <= 10:
    i += 1
    if i == 7:
        continue
    print(i) # // Output ???

# ab tu bolega break main " i += 1 " main niche likha tha aur ya pe upar ye kaise ?? samj mai aayega , dekh practice se khud ba khud samaj mai aayega ,
# aur iska logic hai samjata hu,
# break main hame pure code ya bol sakte hain saare numbers ko check karna tha aur last tak print karna tha jaha pe condition true mil gayi waha pe break laga na tha uske aage nahi jana tha , to code kya karta hai 
# jaise he hame condition true mil gayi waha pe break lagat deta hai aur aage wali numbers print nahi karne to ye aage nahi jane deta break, hame yaha pe last tak aana padega kyu ki hamne add 1 karna hai kab tak , 
# jab tak condition true na mile to jaise he condition true mil jayegi break lag jayega aur loop nich tak nahi aayega , agar nich aagya to code main aur + 1 ho jayega na , break statement se upar he rukjayega , aur loop
# use nich vaale code tak nahi aane dega.

# pr

# continue main waise nahi hota hamne bass us number ko skip karna padta hai aur aage ke numbers bhi print karne hote hai , isliye hamne " i += 1 " ko upar he likhna hota hai 
# taaki upar ke par loop chalta rahe last tak , condition true aane ke baad bhi aage vaala loop to chalana padega na last tak 
# jaise he condition true mil jayegi "i == 7" to use skip kar dega aur fir se upar ke upar loop chalta rahega jab tak last tak na chala jaye.

# ==========================================
# USER INPUT + BREAK 
# ==========================================

# example.
while True:
    name = input("Enter name : ")
    if name == "jaanu":
        print("Correct name") # // Output ???
        break

# ye loop chalta rahega jab tak condition true na ho jaye 
# condition hai name == jaanu 

# ==========================================
# USER INPUT + CONTINUE
# ==========================================

#example.
for i in range(1):
    name = input("enter name : ")
    if name == " ":
        continue
    print("hi",name) # // Output ???


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1) 
for i in range(1, 11):
    if i == 7:
        break
    print(i) # // Output ???

# 2)
for i in range(1, 6):
    if i == 4:
        continue
    print(i) # // Output ???

# 3)
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i) # // Output ???

# 4)
i = 1
while i <= 10:
    if i == 5:
        break
    print(i) # // Output ???
    i += 1

# 5)
for letter in "PYTHON":
    if letter == "T":
        break
    print(letter) # // Output ???


# ==========================================
# MINI PROJECT
# ==========================================
while True:

    password = input("Enter Password : ")

    if password == "python123":
        print("Access Granted")
        break

    print("Wrong Password") # // Output ???




# to finally aaj hamar day 15 complete bhaii ye topic sach main easy hai agar live samju to samaj mai aayega pr ye
# typing karna padta hai to acche se samjna mushkil hai , pr agar dhyan se kiya to samjna possible hai ,
# impossible to bilkul nahi , aur ha day 14 aur day 15 ko daily revise karte ja okay .
# to chal milte hai next lecture main kisi new topic ke saath , tab tak ke liye 


# JAI HIND 
# JAI BHARAT