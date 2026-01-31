import random

def get_fortune():
    fortunes = [
        "You will ace your next coding interview.",
        "A bug-free deployment is in your near future.",
        "Your next pull request will be approved on the first try.",
        "Your tests will pass on the first run.",
        "Someone will call your solution clean.",
        "You will remember the exact command you need on the first try.",
        "Your code review comment will save the team hours.",
        "A large sum of money is coming your way.",
    ]
    return random.choice(fortunes)

if __name__ == "__main__":
    print("🥠 Fortune Cookie Generator 🥠")
    print(f"\nYour fortune: {get_fortune()}")
