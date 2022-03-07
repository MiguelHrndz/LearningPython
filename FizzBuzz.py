for number in range(1,101):
    if number%3 == 0 :
        if number%5 == 0:
         print(number, "\nFizzBuzz")
        else :
         print(number,"\nFizz")
    if number%5 == 0 :
        if number%3 == 0 :
         print(number,"\nFizzBuzz")
        else :
         print(number,"\nBuzz")