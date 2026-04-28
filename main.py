import random

# ASCII art for Rock, Paper, Scissors
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

# List to store all choices
choices = [rock, paper, scissors]

# Score counters
user_wins = 0
computer_wins = 0
draws = 0

# Round counter
round_no = 1

print("🎮 Welcome to Rock–Paper–Scissors Game! 🎮")

# Game loop
while True:
    print(f"\n🔁 Round {round_no}")

    # Taking user input safely
    try:
        user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    # Input validation
    if user_choice < 0 or user_choice > 2:
        print("❌ Invalid choice! Choose 0, 1, or 2.")
        continue

    # Display user's choice
    print("\nYou chose:")
    print(choices[user_choice])

    # Computer randomly selects a choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    # Game logic to determine winner
    if user_choice == computer_choice:
        print("🤝 It's a Draw!")
        draws += 1
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        print("🎉 You Win this round!")
        user_wins += 1
    else:
        print("💻 Computer Wins this round!")
        computer_wins += 1

    # Display scoreboard after each round
    print("\n📊 Current Scoreboard:")
    print(f"You: {user_wins} | Computer: {computer_wins} | Draws: {draws}")

    # Ask user if they want to continue
    play_again = input("\nDo you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        break

    round_no += 1

# Final result summary
print("\n🏁 Game Over!")
print("📊 Final Score:")
print(f"You won: {user_wins} times")
print(f"Computer won: {computer_wins} times")
print(f"Draws: {draws}")

# Overall winner announcement
if user_wins > computer_wins:
    print("🏆 Overall Winner: YOU! Congratulations 🎉")
elif computer_wins > user_wins:
    print("🏆 Overall Winner: COMPUTER 💻")
else:
    print("🏆 Overall Result: It's a TIE 🤝")

print("\n🙏 Thanks for playing Rock–Paper–Scissors!")
