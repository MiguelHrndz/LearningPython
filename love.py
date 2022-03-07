# 🚨 Don't change the code below 👇
from typing import Counter


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# function lower
a = name1
lower1 = a.lower()
b = name2
lower2 = b.lower()

#function count true lower1
c1,e1,f1,g1 = lower1.count('t'),lower1.count('r'),lower1.count('u'),lower1.count('e')
conttrue1 = c1 + e1 + f1 + g1

#function count love lower2
z2,x2,v2,n2 = lower2.count('l'),lower2.count('o'),lower2.count('v'),lower2.count('e')
contlove1 = z2 + x2 + v2 + n2

#function count true lower2
c12,e12,f12,g12 = lower2.count('t'),lower2.count('r'),lower2.count('u'),lower2.count('e')
conttrue12 = c12 + e12 + f12 + g12

#function count love lower1
z22,x22,v22,n22 = lower1.count('l'),lower1.count('o'),lower1.count('v'),lower1.count('e')
contlove22 = z22 + x22 + v22 + n22

low = str(int(conttrue1+conttrue12)) + str(int(contlove1+contlove22))
low = int(low)

print (low)

if low < 10 or low > 90 :
 print (f"Your score is {low}, you go together like coke and mentos.")
elif low >= 40 and low <= 50 :
  print (f"Your score is {low}, you are alright together.")
else :
   print (f"Your score is {low}.")
  

#The lower() function changes all the letters in a string to lower case.
#The count() function will give you the number of times a letter occurs in a string.