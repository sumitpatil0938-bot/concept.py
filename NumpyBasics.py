# ==========================================
#        DAY 36 NUMPY BASICS
# ==========================================
# to kya ghaal chal bhai log kaise ho ,
# firse swagat hai day 36 main.
# aaj ham padhne ja rahe hain numpy ke baare main.
# pehli baar naam sunke lag sakta hai ki ye list , tuple aur
# dictionary ka hi topic hoga.
# lekin aisa nahi hai
# numpy python ka ek specila module hai jo hame
# kuch powerful data structure deta hai.
# inse hamare code aur fast , clean aur easy ho jata hai.
# to bina kisi time pass kiye shuru karte hai.


# ==========================================
#      NUMPY KYA HOTA HAI ?
# ==========================================
# simple language me.
# numpy python ka built-in module hai.
# ye large amount of numerical data ko fast aur efficiently process karne ka liye use hoti hai.
# simple definition yaad rakh.
# Numpy = Numerical python lobrary jo fast mathematical operators ke liyeuse hoti hai.

# Numpy = (Numerical python)


# ==========================================
# NUMPY KI ZARURAT KYU PADTI HAI ?
# ==========================================
# python me list to alreday thi.
# Q) fir numpy banana ki kya zarurat thi???
# --> Normal python list slow hoti hai jab n=bahut bda data process karna ho tab han numpy ka use karte hai.
# - faster hota hai.
# - Kam memory use karte hai.
# - Mathematical opertaions bahut jaldi karte hai.

# Real life example.
# socho 10 students ke marks hai
# ye list me store ho gaye.
# agar 10 crore students ke marks processs karna hain
# tab python list slow pad sakti hai.
# Numpy isi problem ko solve karta hai.


# ==========================================
# NUMPY INSTALL KAISE KARE ??
# ==========================================
# agar install nahi hai to karlo 
# mai bataung
# apne device me terminal pen karo 
# aurr usmai command likho
# --> pip install numpy
# insatll hone ke baad apne code me import karlo
# --> import numpy as np
# numpy --> original library ka naam
# np --> alias name hai jo hamne diya hai , almost sabhi log np ka use karte hai.


# ==========================================
# PEHLA NUMPY ARRAY
# ==========================================
# example.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# // Output ???

# kya hua ??
# step by step 
# --> np.array()
# list ko numpy arrya me convert karta hai.
# simple hai bhi log.


# ==========================================
# LIST VS ARRAY
# ==========================================
# list aur array me kya difference hai ??
# 1) list me alag alag data type store kar sakte hai.
# example.
list1 = [1, 2, 3, "hello", 4.5]
print(list1)
# // Output ???
# 2) lekin array me alag alag data type store nahi kar sakte hai.
# example.
arr1 = np.array([1, 2, 3, "hello", 4.5])
print(arr1)
# // Output ???
# 3) array me mathematical operations bahut jaldi karte hai.
# example.
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([6, 7, 8, 9, 10])
print(arr2 + arr3)
# // Output ???

# dono dekhne me similar hai 
# lekin andar s completely alag hai.


# ==========================================
# ARRAY KA TYPE CHECK KARNA 
# ==========================================
#example.
import numpy as np
arr = np.array([1,2,3,4,5])
print(type(arr))
# // Output ???

# output main jo (ndarray) ka matlab hai
# N-Dimensional array


# ==========================================
# ARRAY INDEXING AND SLICING
# SIZE, SHAPE AND DIMENSIONS
# ==========================================
# same to same jaise hamne list hamne padha tha bass 
# waisa he hai.
# example.
import numpy as np
sumit = np.array([10,20,30,40,50,60,70,80,90,100])
print(sumit[0])
print(sumit[3])
print(sumit[-1]) # negative indexing
print(sumit[1:4]) # slicing
print(sumit[::2]) # step slicing
print(sumit[::-1]) # reverse slicing
print(sumit[1:5:2]) # step slicing
print(sumit[1:]) # slicing from index 1 to end
print(sumit[:5]) # slicing from start to index 4
print(sumit[:]) # slicing from start to end
print(sumit.size) # size of array

print(sumit.shape) # shape of array
# Shape = (10,) means one-dimensional array with 10 elements.

print(sumit.ndim) # number of dimensions
# matlab 1-D array hai.


# ==========================================
# MTHEMATICAL OPERATIONS
# ==========================================
# example.
import numpy as np
ved = np.array([10,20,30,40,50])
print(ved + 10) # add 10 to each element
print(ved - 10) # subtract 10 from each element
print(ved * 2) # multiply each element by 2
print(ved / 2) # divide each element by 2
print(ved ** 2) # square each element

# 1) SUM 
# example.
import numpy as np 
numbers = np.array([1,2,3,4,5])
print(np.sum(numbers)) # sum of all elements
# // Output ???

# 2) MAX
# example.
import numpy as np
numbers = np.array([1,2,3,4,5])
print(np.max(numbers)) # maximum element
# // Output ???

# 3) MIN
# example.
import numpy as np
numbers = np.array([1,2,3,4,5])
print(np.min(numbers)) # minimum element
# // Output ???

# 3) MEAN
# example.
import numpy as np
numbers = np.array([1,2,3,4,5])
print(np.mean(numbers)) # mean of all elements
# // Output ???


# ==========================================
# REAL LIFE USE OF NUMPY
# ==========================================
# Numpy ka use hota hai.
# - Data Analysis
# - Machine Learning
# - Cybersecurity
# - Banking Software
# - Search Engines
# - Large Data Processing
# - Web Applictaions
# - Robotics
# - Artificial Intelligence
# - Image Processing
# - Scientific Computing
# - Data Visualization
# - Computer research

# Almost har AI aur ML project me numpy ka use hota hai.


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2) 
import numpy as np

arr = np.array([10,20,30])

print(arr.size)

# // Output ???

# 3) NumPy ka full form kya hai ??

# 4) NumPy import karne ke liye kya likhenge ??

# 5) Array aur List me ek difference batao.


# ==========================================
# MINI PROJECTS
# ==========================================
import numpy as np 
marks = np.array([10,20,30,40,50])
# 1) marks ka sum nikalna hai.
print(np.sum(marks))
# 2) marks ka mean nikalna hai.
print(np.mean(marks))
# 3) marks ka maximum nikalna hai.
print(np.max(marks))
# 4) marks ka minimum nikalna hai.
print(np.min(marks))
# 5) marks ka square nikalna hai.
print(marks ** 2)
# 6) marks ka reverse nikalna hai.
print(marks[::-1])
# 7) marks ka size nikalna hai.
print(marks.size)
# 8) marks ka shape nikalna hai.
print(marks.shape)
# 9) marks ka dimension nikalna hai.
print(marks.ndim)


# NumPy = Numerical Python Library jo Fast Mathematical Operations ke liye use hoti hai.
# import numpy as np
# np.array()
# np.sum()
# np.max()
# np.min()
# np.mean()

# To finally aaj hamar day 36 khatam hota hai.
# aur aaj ka topic bohat easy tha.
# aur aaj ka topic aage aane vaale project main asbe important
# topic hai to acche se practice karna aur samj na 
# to milte hai day 37 main kisi new topic ke saath.
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳