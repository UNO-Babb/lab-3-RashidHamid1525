#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  
  while True:
        user_choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
        if user_choice not in ["R", "P", "S"]:
            print("Invalid input. Please choose R, P, or S.")
            continue

        computer_choice = random.choice(["R", "P", "S"])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (user_choice == "R" and computer_choice == "S") or \
             (user_choice == "P" and computer_choice == "R") or \
             (user_choice == "S" and computer_choice == "P"):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "N":
            break

  
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
