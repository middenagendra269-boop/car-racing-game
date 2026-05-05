import random

print("=== ROCK PAPER SCISSORS ===")
options = ["rock", "paper", "scissors"]

you = input("rock/paper/scissors? ").lower()
cpu = random.choice(options)
print("Computer:", cpu)

if you == cpu:
    print("Draw")
elif you=="rock" and cpu=="scissors" or you=="paper" and cpu=="rock" or you=="scissors" and cpu=="paper":
    print("You WIN!")
else:
    print("You lose")

input("Press Enter to exit")