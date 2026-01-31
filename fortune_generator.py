import random

def get_fortune():
    fortune_categories = {
        "career": [
            "You will ace your next coding interview.",
            "A bug-free deployment is in your near future.",
            "Your next pull request will be approved on the first try."
        ],
        "learning": [
            "A new programming language will soon capture your interest.",
            "Documentation will become your best friend this week."
        ],
        "wisdom": [
            "The best code is code you don't have to write.",
            "Rubber duck debugging will solve your next problem."
        ]
    }
    
    all_fortunes = [fortune for category in fortune_categories.values() for fortune in category]
    return random.choice(all_fortunes)

def get_lucky_numbers():
    return sorted(random.sample(range(1, 50), 6))

if __name__ == "__main__":
    print("🥠 Fortune Cookie Generator 🥠")
    print(f"\nYour fortune: {get_fortune()}")
    print(f"Lucky numbers: {', '.join(map(str, get_lucky_numbers()))}")
