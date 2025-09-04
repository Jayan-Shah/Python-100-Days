import random
import my_module


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

game = [rock,paper,scissors]

User_choice = int(input("Enter your choice... 0 for rock, 1 for paper and 2 for scissors: "))
print(f"\n User Choose:\n{game[User_choice]}\n")


Computer_choice=random.randint(0,2)
print(f"\nComputer Choose:\n{ game[Computer_choice] }\n")


if User_choice == Computer_choice:
    print("Game Draw")

elif User_choice == 0 :
    if Computer_choice == 1:
        print("You Lost")
    else:
        print("You won")

elif User_choice == 1:
    if Computer_choice==2:
       print("You Lost")
    else:
        print("You won")

elif User_choice == 2:
    if Computer_choice == 0:
        print("You Lost")
    else:
        print("You Won")

else:
    print("Wrong Choice")

