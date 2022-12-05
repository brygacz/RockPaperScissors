import random

while True:
  choices = ["rock","paper","scissors"]
  player = None

  computer = random.choice(choices)

  while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

  if player == computer:
      print("computer: ", computer)
      print("player: ", player)
      print("Remis!")
  elif player == "rock":
    if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You have lost!")
    if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You have won!")
  elif player == "paper":
    if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You have won!")
    if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You have lost!")
  elif player == "scissors":
    if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You have won!")
    if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You have lost!")

  play_again = input("Would you like to play again? (yes/no): ").lower()
  if play_again != "yes":
    break
print("Bye!")