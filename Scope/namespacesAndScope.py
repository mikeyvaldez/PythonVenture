#!/usr/bin/env python3


enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()
# print(pot_strength)


# Global Scope
player_health = 10
def game():
    # The function below is local scope within game function
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)
