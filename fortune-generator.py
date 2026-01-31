import random

def get_fortune():
    fortunes = [
        "You will ace your next coding interview.",
        "A bug-free deployment is in your near future.",
        "Your next pull request will be approved on the first try."
    ]
    return random.choice(fortunes)

if __name__ == "__main__":
    print("🥠 Fortune Cookie Generator 🥠")
    print(f"\nYour fortune: {get_fortune()}")
