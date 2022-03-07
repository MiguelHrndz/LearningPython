rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

selection = print(input("Let's play rock, paper and scissors, What do you will pick?, type 0 for rock, type 1 for paper or type 2 for scissors"))
selection = int
rndom = random.randint(0, 2)
pickbot = int(rndom)

if selection == 0 and rndom == 0 :
    print ("Draw")
elif selection == 0 and rndom == 1 :
    print("You lose")
elif selection == 0 and rndom == 2 :
    print("You win")
elif selection == 1 and rndom == 0 :
    print("You win")
elif selection == 1 and rndom == 1 :
    print ("Draw")
elif selection == 1 and rndom == 2 :
    print("You lose")
elif selection == 2 and rndom == 0 :
    print("You lose")
elif selection == 2 and rndom == 1 :
    print("You win")
elif selection == 2 and rndom == 2 :
    print ("Draw")
