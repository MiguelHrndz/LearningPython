# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
lst = []
lst.append(names_string)
cont = (len(names))
a = random.randint(1, cont)
a = a - 1
print(f"{names[a]} is going to buy the meal today!")


