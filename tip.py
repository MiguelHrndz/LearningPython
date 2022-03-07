print("Welcome to the tip calculator.")
# Ingreso de variables
tip = float(input("What was the total bill?"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = float(input("How many people to split the bill?"))
# Calcular
percentage = float(percentage)
b = float(percentage/100)  
percentagecal = tip * b
tipfinal = tip + percentagecal
each = tipfinal/people
print(f"Each person should pay {each}")