import random
print ("HELLO BUDDY! WANNA PLAY ROCK, PAPER, SCISSOR? MAKE SELECTION PLEASE")
my_selection = input ("rock, paper, scissor? ")
def select_option_randomly():
  return random.choice(["rock","paper","scissor"])
compt_selection = select_option_randomly()
if my_selection == "rock" and compt_selection == "paper":
  print ("YOU LOSE!")
elif my_selection == "rock" and compt_selection == "scissor":
  print ("YOU WIN!")
elif my_selection == "paper" and compt_selection == "scissor":
  print ("YOU LOSE!")
elif my_selection == "paper" and compt_selection == "rock":
  print ("YOU WIN!")
elif my_selection == "scissor" and compt_selection == "rock":
  print ("YOU LOSE!")
elif my_selection == "scissor" and compt_selection == "paper":
  print ("YOU WIN!")
else: print ("TRY AGAIN!")
print ("YOU:", my_selection, "COMPUTER:", compt_selection)