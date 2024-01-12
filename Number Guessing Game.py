import random

def main():
    PlayerChoice = 0
    ComputerChoice = random.randrange(10)
    while PlayerChoice != ComputerChoice:
        PlayerChoice = get_number_from_User()
        if PlayerChoice == ComputerChoice:
            print("Congrats, you're win!")
        elif PlayerChoice > ComputerChoice:
            print("Too much")
        elif PlayerChoice < ComputerChoice:
            print("Too small")
        else:
            print("Error")

def get_number_from_User():
    player_number = int(input("Try to guess a number in the range from 0 to 10: "))
    return player_number

if __name__ == '__main__':
    main()