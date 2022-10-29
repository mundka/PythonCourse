import random
from time import sleep

pc_number = None
game_ended = False

def random_number():
    random_number = random.choice(pc_number)
    return random_number

print("Welcome to the guessing game")
sleep(0.5)
print("You need to guess the number of the computer...")
sleep(0.5)
level = input(f"Please select difficulty: 1(Easy), 2(OK), 3(Impossible)")
level_chk = level.isnumeric()
attempts = 0

if int(level) == 1:
    pc_number = range(1, 4)
    print("you selected EASY level. Guess number from 1-3 ")
elif int(level) == 2:
    pc_number = range(1, 6)
    print("you selected NORMAL level. Guess number from 1-5 ")
elif int(level) == 3:
    pc_number = range(1, 11)
    print("you selected HARD level. Guess number from 1-10 ")
else:
    print("wrong level number!")

while not game_ended:
    attempts += 1
    computers_number = random_number()
    players_number = input("Guess computer's number: ")
    if int(players_number) == computers_number:
        print(f"Computer says: {computers_number}, you say: {players_number}")
        print("You won with {0} attempts \n".format(attempts))
        attempts = 0
        while True:
            another_round = input("Play another round? (y/n)")
            if another_round == "y":
                game_ended = False
                level = input(f"Please select difficulty: 1(Easy), 2(OK), 3(Impossible")
                if int(level) == 1:
                    pc_number = range(1, 4)
                    print("you selected EASY level. Guess number from 1-3 ")
                elif int(level) == 2:
                    pc_number = range(1, 6)
                    print("you selected NORMAL level. Guess number from 1-5 ")
                elif int(level) == 3:
                    pc_number = range(1, 11)
                    print("you selected HARD level. Guess number from 1-10 ")
                break
            elif another_round == "n":
                game_ended = True
                break
            else:
                print("Wrong option.")

    else:
        print(f"Computer says: {computers_number}, you say: {players_number}")

print("Thank you for the game!")
