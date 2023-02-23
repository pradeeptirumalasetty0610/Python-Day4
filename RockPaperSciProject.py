import random as rand
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

game_data=[rock,paper,scissors]

user_input=input('What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')
user_game=game_data[int(user_input)]
print(user_game)

comp_input=rand.randint(0,2)
comp_game=game_data[comp_input]
print('Computer chosen')
print(comp_game)

if (comp_game==paper and user_game==rock) or (comp_game==scissors and user_game==paper) or (comp_game==rock and user_game==scissors):
    print('You lose')
elif (user_game==paper and comp_game==rock) or (user_game==scissors and comp_game==paper) or (user_game==rock and comp_game==scissors):
    print('You win')
elif user_game == comp_game:
    print('Tie')
