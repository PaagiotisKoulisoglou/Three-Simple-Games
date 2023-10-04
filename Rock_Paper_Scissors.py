import random

player_score = 0
cpu_score = 0

print("Three points win the game!")

while player_score < 3 and cpu_score < 3:
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("Rock, Paper, or Scissors? ").lower()

    print(f"Cpu: {cpu_choice}")

    if player_choice == cpu_choice:
        print("It's a tie! No points awarded.")
    elif (player_choice == "rock" and cpu_choice == "scissors") or \
         (player_choice == "paper" and cpu_choice == "rock") or \
         (player_choice == "scissors" and cpu_choice == "paper"):
        player_score += 1
        print("You win this round!")
    else:
        cpu_score += 1
        print("Cpu wins this round!")

    print(f"Score - You: {player_score}, Cpu: {cpu_score}")

if player_score == 3:
    print("You win the game!")
else:
    print("Cpu wins the game!")
