import importlib

def run_game1():
    game1 = importlib.import_module('dino.py')
    game1.run()

def run_game2():
    game2 = importlib.import_module('space_game.py')
    game2.run()

def menu():
    print("-------------------------------------")
    print("|                                   |")
    print("|------Welcome to Game Center-------|")
    print("|                                   |")
    print("|----made by <Full_Snack_Devs/>-----|")
    print("|                                   |")
    print("|------Please choose a game:--------|")
    print("|                                   |")
    print("|-----------1. Dino-----------------|")
    print("|-----------2. Space Game-----------|")
    print("|                                   |")
    print("-------------------------------------")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        run_game1()
    elif choice == '2':
        run_game2()
    else:
        print("Invalid choice. Please try again.")

# Run the menu
menu()
