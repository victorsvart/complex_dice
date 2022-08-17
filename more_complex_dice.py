import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')


def dice():
    while True:
        user = input("\nDo you want to roll dices? (Y/N): ")

        # The User Decides = Yes --------------------------------------------------------

        if user.lower() in ['yes', 'y']:
            dice_amount_choice = input("How many? (Max of 6): ")
            dice_number = ""
            os.system('cls' if os.name == 'nt' else 'clear')

            if (dice_amount_choice in ['1', '2', '3', '4', '5', '6']):
                dice_amount_choice = int(dice_amount_choice)

                for dice_number in range(dice_amount_choice):
                    dice_number = random.randrange(1, 7)
                    print(f"Dice rolled! You got: {dice_number}")
                    time.sleep(1)

            elif (dice_amount_choice in ['one', 'two', 'three', 'four', 'five', 'six']):

                dice_amount_choice = (1 if dice_amount_choice == 'one' else 2 if dice_amount_choice == 'two'
                                      else 3 if dice_amount_choice == "three" else 4 if dice_amount_choice ==
                                      "four" else 5 if dice_amount_choice == "five" else 6 if dice_amount_choice ==
                                      "six" else exit())

                for dice_number in range(dice_amount_choice):
                    dice_number = random.randrange(1, 7)
                    print(f"Dice rolled! You got: {dice_number}")
                    time.sleep(1)
            # Out Of Bounds Value
            else:
                print("Out of range...")
                continue

            # --------------------------------------------------------------------------------

        # The User Decides = No -------------------------------------------------------------

        elif user.lower() in ['no', 'n']:
            print("Heading back to menu...\n")
            return
        # Invalid prompt
        else:
            print("Invalid answer, try again:\n ")

        # ----------------------------------------------------------------------------------


#  MAIN FUNCTION ---------------------------------------------------------------------------


def main():
    while True:
        print("Welcome to Victor's Dice Roller!\n1 - Dice Roll\n2 - Exit")
        choice = int(input("\nChoose: "))
        if (choice == 1):
            dice()
        elif (choice == 2):
            print("See you next time!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        else:
            print("Invalid input. Please try again.\n")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')


main()
