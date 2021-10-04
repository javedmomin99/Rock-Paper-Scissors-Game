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
print("Welcome to the Rock - Paper - Scissors Game")
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game_images = [rock, paper, scissors]
if user_choice == 0 or user_choice == 1 or user_choice == 2:
  print(game_images[user_choice])
  import random
  computer_choice = random.randint(0,2)
  print("Computer chose :")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 0:
    print("It's a Draw")
  elif user_choice == 0 and computer_choice == 1:
    print("You Lose!")
  elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
  elif user_choice == 1 and computer_choice == 1:
    print("It's a draw")
  elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")
  elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
  elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
  elif user_choice == 2 and computer_choice == 2:
    print("It's a Draw")
else:
  print("You typed an invalid number, you lose!")
