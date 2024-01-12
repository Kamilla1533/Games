import random

def main():
    user_choice = show_selection_items()
    computer_choice = generate_random_numbers()
    conditions_for_winning(user_choice, computer_choice)


def another_round():
    user_choice = show_selection_items()
    computer_choice = generate_random_numbers()
    conditions_for_winning(user_choice, computer_choice)

def show_selection_items():
       print("if you want to select a rock, then press 1")
       print("if you want to select a scissors, then press 2")
       print("if you want to select a paper, then press 3")
       UserChoice = int(input("Enter your selection value: "))
       return UserChoice

def generate_random_numbers():
    ComputerChoice = random.randint(1, 3)
    print(f"The computer chose value {ComputerChoice}")
    return ComputerChoice

def conditions_for_winning(userChoice, computerChoice):
    if userChoice == 1 and computerChoice == 2:
        print("Rock beats scissors")
        print("User is win")
        return userChoice, computerChoice
    elif userChoice == 2 and computerChoice == 1:
        print("Rock beats scissors")
        print("Computer is win")
        return userChoice, computerChoice
    elif userChoice == 2 and computerChoice == 3:
        print("Scissors beats paper")
        print("User is win")
        return userChoice, computerChoice
    elif userChoice == 3 and computerChoice == 2:
        print("Scissors beats paper")
        print("Computer is win")
        return userChoice, computerChoice
    elif userChoice == 3 and computerChoice == 1:
        print("Paper beats rock")
        print("User is win")
        return userChoice, computerChoice
    elif userChoice == 1 and computerChoice == 3:
        print("Paper beats rock")
        print("Computer is win")
        return userChoice, computerChoice
    elif userChoice == computerChoice:
        print("Your answers are equal")
        print("One more round is needed to determine the winner")
        print("Continue? (enter yes or no)")
        answer = str(input())
        if answer == "yes":
            print("We announce a new round!")
            while answer == "yes":
                another_round()
        else:
            print("Goodbye, coward...")
    else:
        print("Unacceptable value")

if __name__ == '__main__':
    main()