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

myList = [rock, paper, scissors]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(myList[player_choose])
computer_choose = random.randint(0, 2)
print("Computer choose:")
print(myList[computer_choose])
if player_choose == computer_choose:
    print("It's a draw")
else:
    if player_choose == 0:
        if computer_choose == 1:
            print("You loose")
        elif computer_choose == 2:
            print("You win!")
    elif player_choose == 1:
        if computer_choose == 0:
            print("You win!")
        elif computer_choose == 2:
            print("You loose")
    else:
        if computer_choose == 0:
            print("You loose")
        elif computer_choose == 1:
            print("You win!")
