import random

class MagicPotion:
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency
    
    def drink(self):
        if self.potency > 0:
            print(f"Drank {self.name}. Feel invigorated!")
            self.potency -= 1
        else:
            print(f"No more {self.name} left!")
    
    def refill(self):
        print(f"Refilling {self.name}.")
        self.potency = random.randint(1, 5)

# Create two MagicPotion objects
healing_potion = MagicPotion("Healing Potion", 3)
strength_potion = MagicPotion("Strength Potion", 2)

# Game loop
while True:
    print("\n=== Magic Potion Game ===")
    action = input("What would you like to do? (drink_healing, drink_strength, refill, quit): ")

    if action == "drink_healing":
        healing_potion.drink()
    elif action == "drink_strength":
        strength_potion.drink()
    elif action == "refill":
        choice = input("Refill which potion? (healing, strength): ")
        if choice == "healing":
            healing_potion.refill()
        elif choice == "strength":
            strength_potion.refill()
        else:
            print("Invalid choice.")
    elif action == "quit":
        print("Exiting game.")
        break
    else:
        print("Invalid action.")
