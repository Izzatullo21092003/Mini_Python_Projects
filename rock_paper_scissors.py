import random as rd

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

game_image = [rock, paper, scissors]
user_ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_ch = rd.randint(0, 2)
print(game_image[user_ch])
print(game_image[computer_ch])
if user_ch == 0:
    if computer_ch == 1:
        print("You lose!")
    elif computer_ch == 2:
        print("You win!")
    else:
        print("Draw")
elif user_ch == 1:
    if computer_ch == 0:
        print("You win!")
    elif computer_ch == 2:
        print("You lose!")
    else:
        print("Draw")
elif user_ch == 2:
    if computer_ch == 0:
        print("You lose!")
    elif computer_ch == 1:
        print("You win!")
    else:
        print("Draw")
else:
    print("Invalid choice!")
