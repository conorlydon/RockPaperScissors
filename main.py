import fontstyle

print(
  fontstyle.apply('WELCOME TO ROCK PAPER SCISSORS',
                  'bold/Italic/red/GREEN_BG\n'))


def loading():
  import sys
  import time

  a = 0
  for x in range(0, 3):
    a = a + 1
    b = ("Loading" + "." * a)
    # \r prints a carriage return first, so `b` is printed on top of the previous line.
    sys.stdout.write('\r' + b)
    time.sleep(1)
  print(a, "seconds, thanks for waiting!")


import time
# Rock Paper Scissors ASCII Art
# Rock
time.sleep(1.5)
rock = ("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

# Paper
paper = ("""
     _______
 ---'   ____)____
           ______)
           _______)
         _______)
 ---.__________)
 """)

# Scissors
scissors = ("""
     _______
 ---'   ____)____
           ______)
       __________)
      (____)
---.__(___)
""")

import time

possible_actions = ["rock", "paper", "scissors"]
print ("ROCK!",(rock)), (time.sleep(1))
print ("PAPER!",(paper)),(time.sleep(1))
print ("SCISSORS!",(scissors)),(time.sleep(1))

possible_actions = ["rock", "paper", "scissors"]

import random

all_list = []
all = open("all.csv", "a")


analysis_heading = fontstyle.apply('YOUR ANALYSIS', 'bold/Italic/red/GREEN_BG')


def game():
  user_action = input("Enter a choice (rock, paper, scissors): ").lower()
  possible_actions = ["rock", "paper", "scissors"]
  computer_action = random.choice(possible_actions)
  print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

  if user_action == computer_action:
    if user_action == "rock":
      all_list.append(possible_actions[0])
     
      print(rock)
      print(rock)
    elif user_action == "paper":
      
      all_list.append(possible_actions[1])
      print(paper)
      print(paper)
    elif user_action == "scissors":
      
      all_list.append(possible_actions[2])
      print(scissors)
      print(scissors)
    print(f"Both players selected {user_action}. It's a tie!")
    #rock
  elif user_action == "rock":
    all_list.append(possible_actions[0])
    print(rock)
    if computer_action == "scissors":
     
      print(scissors)
      print("Rock smashes scissors! You win!")
    else:
      
      print(paper)
      print("Paper covers rock! You lose.")
    #paper
  elif user_action == "paper":
    all_list.append(possible_actions[1])
    print(paper)
    if computer_action == "rock":
      
      print(rock)
      print("Paper covers rock! You win!")
    else:
      
      print(scissors)
      print("Scissors cuts paper! You lose.")
    #scissors
  elif user_action == "scissors":
    all_list.append(possible_actions[2])
    print(scissors)
    if computer_action == "paper":
      
      print(paper)
      print("Scissors cuts paper! You win!")
    else:
      
      print(rock)
      print("Rock smashes scissors! You lose.")

  else:
    print("Please enter valid answer:")
    game()
#making restart function
  def restart():
    r = input("\nWould you like to play again? yes/no:").lower()
    if r == "yes":
      print("\nNew game commencing...\n_______"), time.sleep(0.5), loading(),
      game()
    elif r == "no":
      print("Ok, Thanks for playing.\n________\n")
    else:
      print("Please enter yes or no.")
      restart()

  restart()


game()
#total data
import csv

print(analysis_heading, "\n________")

#all.write(str(all_list))
#filename = "all.csv"
#total_list = []
#write all list to all.csv
with open('all.csv', 'a', encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(all_list)

total_list = []
with open("all.csv", 'r') as csvfile:  #open csv file
  reader = csv.reader(csvfile)  #read it
  for row in reader:  #iterate through each row
    for item in row:  #iterate through each item of that row
      total_list.append(item)  #add to list
print("These were your moves:", total_list)
rf = total_list.count(possible_actions[0])
pf = total_list.count(possible_actions[1])
sf = total_list.count(possible_actions[2])
freq_list = [rf, pf, sf]
amount_played = rf + pf + sf
if amount_played > 1:
  print("You played", amount_played, "times.")
else:
  print("You played", amount_played, "time.")

print(freq_list)
all.close()
if freq_list[0] > freq_list[1] and freq_list[0] > freq_list[2]:
  print("You chose rock the most.")
elif freq_list[1] > freq_list[2] and freq_list[1] > freq_list[0]:
  print("You chose paper the most.")
elif freq_list[2] > freq_list[1] and freq_list[2] > freq_list[0]:
  print("You chose scissors the most.")
elif freq_list[0] == freq_list[
    1] and freq_list[1] > freq_list[2] and freq_list[1] > freq_list[2]:
  print("You chose rock and paper the most.")
elif freq_list[0] == freq_list[
    2] and freq_list[0] > freq_list[1] and freq_list[2] > freq_list[1]:
  print("You chose rock and scissors the most.")
elif freq_list[1] == freq_list[
    2] and freq_list[1] > freq_list[0] and freq_list[2] > freq_list[0]:
  print("You chose paper and scissors the most.")
print("_________\n")





import matplotlib.pyplot as plt

plt.title("Your Total Moves")
plt.ylabel("Number of times you chose rock paper or scissors")
plt.xlabel("Options")
plt.bar(possible_actions, freq_list)
plt.show()
