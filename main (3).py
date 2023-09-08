#Problem 2.4.4 - Copy and paste link to Canvas once the tests are passed.

import random
choice= int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
comp=random.randint(0,2)

choices=["rock", "paper", "scissors"]
print("You chose", choices[choice] , " and the computer chose",choices[comp])

if choice==comp:
  print("tie")
elif (choice-1)%3==comp:
  print("You win")
else:
  print("You lose")
  