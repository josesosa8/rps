# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random 

option = input("What do you choose? Type 1 for rock, 2 for Paper, 3 for Scissors. ")

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

if option == 1:
    print(rock)
if option == 2: 
    print(paper)
if option == 3:
    print(scissors)

computer = random.randint(0, 2)

print(computer)

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



