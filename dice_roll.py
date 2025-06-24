import random
import time
import os

# Dice faces in ASCII
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_animation():
    print("Rolling the dice", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def print_dice(number):
    for line in DICE_ART[number]:
        print(line)

def main():
    while True:
        input("🎯 Press Enter to roll the dice or type 'q' to quit: ")
        clear_console()
        countdown_animation()
        result = random.randint(1, 6)
        print(f"🎲 You rolled a {result}!")
        print_dice(result)
        print("\n")
        again = input("🔁 Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break
        clear_console()

if __name__ == "__main__":
    main()
