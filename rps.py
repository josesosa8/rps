# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random 

option = input("What do you choose? Type 0 for rock, 1 for Paper, 2 for Scissors. ")

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

print("Your move: ")
if option == "0":
    print(rock)
if option == "1": 
    print(paper)
if option == "2":
    print(scissors)

computer = random.randint(0, 3 - 1)

print("-------------------------------------")
print('Computers move:')

if computer == 0:
    print(rock)
if computer == 1: 
    print(paper)
if computer == 2:
    print(scissors) 

# rock v rock = tie
# scissors v scissors = tie
#paper v paper = tie
# rock v paper = paper
#rock v scissors = rock
# paper v scissors = scissors
# scissors v rock = rock 
if option == "0" and computer == 0:
    print("It\'s a tie. ")
if option == "1" and computer == 1:
    print("It\'s a tie. ")
if option == "2" and computer == 2:
    print("It\'s a tie. ")
if option == "0" and computer == 1:
    print("Computer wins! ")
if option == "1" and computer == 0:
    print("You win! ")
if option == "2" and computer == 0:
    print("Computer wins! ")
if option == "0" and computer == 2:
    print("You win! ")
if option == "1" and computer == 2:
    print("Computer wins! ")
if option == "2" and computer == 1:
    print("You win! ")



