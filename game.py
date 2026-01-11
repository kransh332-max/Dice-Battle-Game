import random
user_score = 0
computer_score = 0
rounds = 5
print("🎲 Welcome to Dice Battle Game 🎲")
for i in range(1, rounds + 1):
    input(f"\nRound {i} - Press Enter to roll the dice ")
    user_dice = random.randint(1, 6)
    computer_dice = random.randint(1, 6)

    print(f"You rolled: {user_dice}")
    print(f"Computer rolled: {computer_dice}")
    if user_dice > computer_dice:
        print("You win this round 🏆")
        user_score += 1
    elif computer_dice > user_dice:
        print("Computer wins this round 🤖")
        computer_score += 1
    else:
        print("It's a tie 🤝")
print("\n🎯 Final Result")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("🎉 You won the game!")
elif computer_score > user_score:
    print("😢 Computer won the game!")
else:
    print("🤝 Game Draw!")
