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

user = int(input("What do you choose?: Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You choose:")

if user == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    
elif user == 1:
    print(
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print(
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    
computer = random.randint(0, 2)
print("Computer choose:")

if computer == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    
elif computer == 1:
    print(
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif computer == 2:
    print(
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if user >= 3:
    print("Invalid choice!")
    
elif user == 0 and computer == 2:
    print("You Win!")

elif user == 1 and computer == 0:
    print("You Won!")

elif user == 2 and computer == 1:
    print("You Won!")
elif user == 0 and computer == 1:
    print("You Lose!")
elif user == 1 & computer == 1:
    print("Tie")
 
elif user == 2 & computer == 2:
    print("Tie")
    
elif user == 0 & computer == 0:
    print("Tie")   
    
else:
    print("You lose!")
    