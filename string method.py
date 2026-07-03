# ==========================================
#          DAY 8 STRING METHODS
# ==========================================

# to yaa haal chal bahi log aagaye vaapas day 8 maine
# to aaj ka hamara topic hain string methods to hmm shurvat se padenge
# aurr ha tu continue kar raha hai na , karle tabhi samja main aayega varna kuch nahi samjega tujhe




# string methods ko hamne day 7 main he cover kar diye hain 
# to firse repeat karne ki jarurat nahi hain , tu use run karle aur samjha main aayega
# aur un question pe practice karle jo maine day 7 main diye hain , to chal ab aage badte hain


# ek kaam kartein day 8 maine ham saare question solve karenge abhi taak hamne jo bhi cover kiya hain day 7 tak uske upar question solve karenge , to chal ab aage badte hain
# to chal ham chat gpt se question lete hain 
# 3 types ke question 1) easy 2) medium 3) hard 
# to chal shuru kartain hain 
# 
# toic jo hamne day 1 - day 7 
#✅ Arrays
#✅ Variables
#✅ Data Types
#✅ Type Casting
#✅ Operators
#✅ User Input
#✅ Strings                    


# ==========================================
# EASY LEVEL
# ==========================================


# 1) Variable name mein apna naam store karo aur print karo.
from turtle import width


name = "sumit"
print(name)

# 2) Do numbers banao aur unka addition print karo.
num1 = 5
num2 = 10
print(num1 + num2)

# 3) String "Python" ka first character print karo.
name = "Python"
print(name[0])

# 4) User se naam lo aur print karo.
name = input("Enter your name: ")
print(name)

# 5) String "SUMIT" ko lowercase mein convert karo.
name = "SUMIT"
print(name.lower())

# 6) List banao:  [10, 20, 30, 40]. Aur first element print karo.
sumit = [10, 20, 30, 40]
print(sumit[0])

# 7) Tuple banao: (1, 2, 3, 4). Aur last element print karo.
sumit = (1, 2, 3, 4)
print(sumit[-1])

# 8) Dictionary banao: {"name": "sumit", "age": 21}. Aur age print karo.
sumit = {"name": "sumit", "age": 21}
print(sumit["age"])

# 9) String "Hello World" mein "World" ko replace karo "Python" se.
name = "Hello World"
print(name.replace("World", "Python"))

# 10) Float value 10.5 ko integer main convert karo aur print karo.
num = 10.5
print(int(num))



# ==========================================
# MEDIUM LEVEL
# ==========================================



# 1) User se do numbers lo aur unka multiplication print karo.
num1 = int(input("enter number : "))
num2 = int(input("Enter number : "))
print(num1 * num2)

# 2) string "python programming" ko upper case maine convert karo 
name = "python programming"
print(name.upper())

# 3) List banao: [1, 2, 3, 4, 5]. Aur last element ko remove karo aur print karo.
sumit = [1, 2, 3, 4, 5]
sumit.pop()
print(sumit)

# 4) Check karo "Mango" in ["Apple", "Banana", "Mango"] 
fruits = ["Apple", "Banana", "grapes"]
if "Mango" in fruits:
    print("Mango is present")
else:
    print("Mango is not present") 

# abhi hamne if else nahi padha hain to nahi samjega , aur samaj gaye to thik hai 

# 5) User se name lo aur uski length print karo.
name = input("Enter your name : ")
print(len(name))

# 6) check karo 20 >= 18 and 20 <= 60 output kya aayrga ?
num = (20 >= 18 and 20 <= 60) # both condition are true 
print(num)

# 7) string "programming" main index 4 ka character print karo 
num = "programming"
print(num[4])

# 8) User se rectangle ki length aur width  lo aur area calculate karo.
lengtha =int(input("Enter length : "))
widtha = int(input("Enter width : "))
area = lengtha * widtha
print("Area of rectangle:", area)

# 9) string "python python python" main "python" kitni baar aaya hai count karo ?
word = ("python python python")
print(word.count("python"))

# 10) List banao: [1, 2, 3, 4, 5]. Aur usme 6 add karo aur print karo.
list = [1, 2, 3, 4, 5]
list.append(6)
print(list)




# ==========================================
# HARD LEVEL
# ==========================================




# 1) User se first name aur last name lo aur full name print karo.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Full name:", full_name)

# 2) user se ek string lo aur uska fir  uppercase , lowercase , length  print karo ?
name = input("Enter your name : ")
print(name.upper())
print(name.lower())
print(len(name))

# 3) user se ek number lo check karo evan hai ya odd , operator use karo (%)?
num = int(input("Enter number : "))
print(num % 2 == 0) # true if even , false if odd

# 4) string "PythonProgramming" mein sirf Programming print karo using slicing 
name = "PythonProgramming"
print(name[6:17])

# 5) user se do number lo aur unka division, addition, subtraction , and multiplication karo 
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

print("Division:", num1 / num2)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)  
print("Multiplication:", num1 * num2)

# 6) list [10, 20, 30, 40, 50] main last value negative indexing se print karo 
list = [10, 20, 30, 40, 50]
print(list[-1])

# 7) string "   Sumit Patil   "  extra space remove kar do 
name = "   Sumit Patil   "
print(name.strip())

# 8) user se sentence lo aur check karo ki "Python" usme hai ya nahi
sentence = input("Enter a sentence: ")
if "Python" in sentence:
    print("Python is present in the sentence.")
else:
    print("Python is not present in the sentence.")

# 9) user se ek decimal number lo aur usse integer main convert karo aur print karo
num = float(input("Enter number : "))
print(int(num))

# 10) user se name , age , city input lo , aur output kuch aisa hona chahiye 
# ----- USER DETAILS -----

# Name : Sumit
# Age  : 21
# City : Pune

# Length of Name : 5
# Name in Uppercase : SUMIT

name = input("Enter name : ")
age = int(input("Entr age : "))
city = input("Enter city : ")

print(len(name))
print(name.upper())




# to finally aaj hamara day 8 complete hogaya 
# to aaj hamne day 8 maine saare question he solve kare hai , kyu ki jo string method jo hai wo ham 
# day 7 maine he pad chuke hai

# aurr ha saare ke saare question solve karke dekh khud se solve karke dekho mine solve keiye hain isliye tu mera dekh ke mat karo 
# tu khud se karoo aur agar nahi smaja aaya to bass overview karlo samjlo kyu hua aisa 
# aur jis question pe atak jaye to vaapas us topic pe ja , dekh use topic ko doubara 
# aur fir solve karrr
# okay 

# to chalo milte hain day 9 maine new topic ke saath 
# tab tak ke liye 
# jai hind 
# jai bharat 

