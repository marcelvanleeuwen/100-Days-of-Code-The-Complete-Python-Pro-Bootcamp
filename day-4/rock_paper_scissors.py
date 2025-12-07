# Rock Paper Scissors

import random

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

# user choice

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

images = [rock, paper, scissors]

if choice < 0 or choice > 2:
    print("Invalid choice")
else:
    print("You chose:")
    print(images[choice])

    # computer choice

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(images[computer_choice])

    # game logic

    if choice == computer_choice:
        print("It's a draw!")
    elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You lose!")
