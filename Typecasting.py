# TYPE CASTING DAY 4 


#  To chalo firse aapka swagat krta hu day 4 main , to aaj hm pdne ja rahe type casting in python kya hota hai ,
# aur haa bahiii/behann log khuch nahi bass daily ke daily karte jao hojayega tension mat leiya karo 
# so back to topic again 
#  so LETS START 


# WHAT IS TYPE CASTING ?
# TYPE CASTING -> ka matlab hai ke ek data type ko doosre data type mein convert karna. 
# easy language mai bole to jab hum kisi value ka data type change karte hain ,usee type casting bolte hai. 


# aurr haa ab ye mat puchna ye data type kya hai , varna etna marunga na  agar nahi pata kya hai data type to to day 3 pr ja maine detail main explain keiya hai kya hai oaky 

# maan lo tumhare pass string hai "25" , ye dekh tu int/number lag raha hai pr python ke liye ye ek 
# string hai kyu ki ise hm ne quote main band keiya hai okay samaj aaya na 
# nahi samja to ek barr firse bol raha hu day 3 mai jake dekh lo 

# agar hame ise solve karna ho ga to 25 ko integer main convert krna padega okay 

num = int(25) # kuch is taraha se karna padega oaky 
# to hme basically kya keiya hai 25 ko ek variable mai store keiya hai "num" aur hmm isee integr main convert karna tha to hmne iske samne int laga diya .
# abb samja kuch , chl thik hai 

# chall ab tu bolega hame kaise pata ye integer hai ya string to iske liye bhi mere pass trick wo bhi bata deta hu KHUSH HO JA 😉
# hm ise ek example ke ssath samjte hai taaki tuje assche se samaj mai aaye dekha dhyan se dekh 
num = "25" # ab python ise string samje ga 
print(type(num)) # agar tu ye code chala ye ga to , dekh tu khud dekh kya output aayega , nahi aya na to mai abhi ke abhi ye series band kar dunga .

# NEXT TOPIC 

# TYPE CASTING FUNCTIONS 
# python mai jayda tr ye function use hote hai 

#. FUNCTIONS.       CONVERT TO 

# 1] int()           integer
# 2] float()         float
# 3] str()           string
# 4] bool()          boolean      



# To chal suru krte hai bina koi time pass keiya 

# 1] STRING ----> INTEGER

# sun iske theory hai lekin ham example se aur acche se smjte hai okay theory to bana leiyo tere mn se , patat hai bana lega tu 👍
 
num = "25" # ye string hai
sumit = int(num) # is step mai , maine jo hamra string(25) tha na use ek variable (sumit) mai store keiya hai 

print(sumit) # to ye bhi krke dekh leiyooo challege hai dekh output 25 as a integer he milega 
print(type(sumit)) # uske saath saath ye bhi print karke dekh 


# chall ek kaam kr ab tu 
# ye print karke dekh 
num = "25"

print(num + 2) # aur ha dekha kya aayega mai to nahi bate ne vaala , agar mai yaha pe bata du to tu khud nahi karega muje pata hai , so krke dekha mere bahii varna khuch samaj mai nahi aayega 
# // output

# To sun mai ab bataunga ab iss problem ko  solve kaise kare 
num = "25" 
print(int(num) + 2) # ab ise run kare dekh kya output aa raha hai samja , kya keiya maine yaha pe 
# kuch alag ya rocket science nahi hai, tu baat ko samaj , yaha pe [ int(num) ] hmne iske help se 25 ko string se integer mai convert keiya jaise hmm abhii kr rahe the aurr usme 2 ko add kr diya , dekha simple hai agar abhi nahi samga to koi baat nahi aage samaj jayega tu , tu 
# bass contine karte ja 


# 2]  INTEGER  ---->  STRING 
# 
# isme kuch nahi karna same to same hai bass ham jaha jaha pe int laga rahe the usko str ke saath replace krde 
# 
# chal example pe jate hai 
# 
num = 56  #Abbb dhyan se dekh maine yaha pe 56 ko as a integer liya hai kyu ki hm integr ko string mai convert kr rahe hai 

age = str(num) # yaha pe hm ne int ko str ke saath replace keiya hai 

print(age) # phir se wahi same steps print karo and --
print(type(age)) # ek barr ise bhi print karke dekh leiyoo


# 3]  INTEGER ----> FLOAT 

# dekh agar tu ne day 1 aur day 2 dekh liya hai to tuje samaj mai aayega varna nahi aayega abhi bata de raha hu 

# chal ab isee acche se samj te hai 


sumit = 10

num = float(sumit) # ab yaha pe kuch nahi ye jo 10 hai uska output flow mai aayega , tu karke dekh leiyoo ek barr oaky 

print(num) # aasan hai ye sab , bass thoda sa jyada nahi bol raha hu mai bass toda sa demak laga le hojayega 

print(type(num)) # ye print krne se tuje pata chal jayeg kisme convert hua hai 



# 4] FLOAT  ---->  INTEGER

## VICEVERSA pata hai bass wahi hai yaha pe 

rohan = 99.99

price = int(rohan) # yaha pe jo int hai na wo jo decimal part hai .99 use remove kar dega 

print(price)

## Dekh main abhii bhi bolta hu tu karlega aur aage jake to tu faad dega bhii , matlab tere aas pass bhi koi nahi hoga , tu alag he leval ka banda hoga tabtak
# bass continu krr 



# 5]  BOOLEAN TYPE CASTING 

# ab meri baat dhyaa se sun okay IMPORTANT hai ye 
# mai jo bolta hu use dhyan mai rakh , jabtak jinda hai tabtak tuje wo yad hona chaiyea


# A) NUMBER TO BOOLEAN --> ZERO KO CHOD KE BAKI SABB "TRUE" HOTE HAI AUR ZERO [ 0 ] "FALSE"
#                       ya fir tu ise aise bhi bol sakta hai  0 KE ALAWA HAR NUMBER TRUE HOTA HAI 
# eg . 
print(bool(100)) # print karke dekh 
print(bool(-5))  #print karke dekh

# B) STRING TO BOOLEAN --> EMPTY  STRING ( " " )  "FALSE"
#                       NON-EMPTY STRING ( "SUMIT" )  "TRUE""
#eg .
print(bool("Sumit")) # print karke dekh 
print(bool(""))  # print karke dekh 

# C) LIST TO BOOLEAN --> EMPTY LIST ( [ ] ) "FALSE"
#                        NON-EMPTY LIST ( [ 1,2,3,4 ] ) "TRUE"
#eg .
print(bool([1, 2, 3]))
print(bool([]))

# D) TUPLE TO BOOLEAN --> EMPTY TUPLE ( ( ) ) "FALSE"
#                        NON-EMPTY TUPLE ( ( 1,2,3,4 ) ) "TRUE"
#eg .
print(bool((1, 2)))
print(bool(()))

# E) DICTIONARY TO BOOLEAN --> EMPTY DICTIONARY ( { } ) "FALSE"
#                        NON-EMPTY DICTIONARY ({"name : ved"}) "TRUE"
#eg .
print(bool({"name": "Sumit"}))
print(bool({}))





# iske liye easy trick hai

# ye sare false banne wali values hai |
#bool(0)
#bool("")
#bool([])
#bool(())
#bool({})
#bool(None)


# // output FALSE 



# ye saare true banne wali values hai
#bool(1)
#bool(100)
#bool("ved")
#bool([1, 2])
#bool((1, 2))
#bool({"name": "ved"})


# // output TRUE

# chall ab tu bata mai to nahi batunga tu bol 
print(bool(1))  # // output kya hoga ???????
print(bool(0))   # // output kya hoga ???????


## bass bhaii ho gaya tera typecasting khatahm 
# waise ek concept hai tu karke dekh to 
age = int(input("Enter age: "))

print(age + 5)  # // solve karke dekh agar samj mai nahi aay to tension mat le aage aayega 

## iska output aayega 

# practice question time 
# 1] 
num = "50"

num = int(num)

print(num)
print(type(num))

# 2]
num = 25

num = str(num)

print(type(num))

# 3]
num = 15

num = float(num)

print(num)

# 4] 
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)


# easy way yaad krne ke liya 

#String  → int()   → Integer
#Integer → float() → Float
#Integer → str()   → String
#Any Type → bool() → Boolean



# Type Casting ka matlab hai ek data type ko doosre data type mein convert karna, jaise String ko Integer mein ya Integer ko String mein convert karna. 

# milte hai day 5 main ☺️





