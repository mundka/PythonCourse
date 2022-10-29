import randomgame

game_ended = False

print("Guess the computers number from 1 to 9")
while not game_ended:
    computers_number = random.randint(1, 5)
    players_number = input("Guess computer's number: ")

    if int(players_number) == computers_number:
        print(f"Computer says: {computers_number}, you say: {players_number}")
        print("You won!")

        while True:
            another_round = input("Play another round? (y/n)")
            if another_round == "y":
                game_ended = False
                break
            elif another_round == "n":
                game_ended = True
                break
            else:
                print("Wrong option.")

    else:
        print(f"Computer says: {computers_number}, you say: {players_number}")

print("Thank you for the game!")