# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap = bool()
if year % 4 == 0 :
    leap = True
    if year % 100 == 0 :
        leap = False
if year % 400 == 0 :
    leap = True
    if year % 100 == 0 :
        leap = False

if leap == False : 
    print("Not leap year.")
elif leap == True :
    print("Leap year.")
  

#El año es un año bisiesto (tiene 366 días).
#El año no es un año bisiesto (tiene 365 días).
#Es bisiesto si es divisible entre 4.
#Pero no es bisiesto si es divisible entre 100.
#Pero sí es bisiesto si es divisible entre 400.