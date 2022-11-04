from time import *
from random import *
# Simple tic-tac-toe game with basic calculations

def fraction():
    n = randint(1, 2)
    while n == 0:
        n = randint(1, 2)
    d = randint(2, 5)
    return str(n) + "+" + str(d)

def problem():
    f1 = fraction()
    f2 = fraction()
    s = choice(["+", "-"])
    print("(" + f1 + ")" + s + "(" + f2 + ")" "=")
    un = int(input("numerator: "))

    answer = eval("(" + f1 + ")" + s + "(" + f2 + ")")

    # check answer
    if abs(answer - un) < 0.000001:
        print("Correct")
        sleep(1)
        return True
    else:
        print("Sorry, incorrect ")
        sleep(1)
        return False


def board(lst, player):
    str = " " + lst[1] + " | " + list[2] + " | " + lst[3] + "   1 2 3"
    str += "\n" + "-" * 11 + "\n"
    str += " " + lst[4] + " | " + list[5] + " | " + lst[6] + "   4 5 6"
    str += "\n" + "-" * 11 + "\n"
    str += " " + lst[7] + " | " + list[8] + " | " + lst[9] + "   7 8 9"
    print(str)


def check(lst):
    for a in range(0, 3):
        if lst[1 + a * 3] != " " and lst[1 + a * 3] == lst[2 + a * 3] == lst[3 + a * 3]:
            return True
        if lst[1 + a] != " " and lst[1 + a] == lst[4 + a] == lst[7 + a]:
            return True
    if lst[1] == lst[5] == lst[9] != " " or lst[3] == lst[5] == lst[7] != " ":
        return True
    return False


list = [" "] * 10
computer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = False
board(list, "x")

while win == False and len(computer) > 0:
    if problem() == True:
        player = "x"
        spot = int(input("place " + player + " at space: "))
        while spot < 1 or spot > 9 or list[spot] != " ":
            spot = int(input("place " + player + " at space: "))
        board(list, player)
        list[spot] = player
        computer.remove(spot)
        win = check(list)
    sleep(1)
    if win == False:
        player = "o"
        c = choice(computer)
        computer.remove(c)
        print("computer picks", c)
        list[c] = player
        board(list, player)
        win = check(list)
    print(" ")
    if computer == []:
        break

board(list, player)
if win == True and player == "x":
    print("You win!!")
elif win == True:
    print("Sorry, the computer wins")
else:
    print("No one wins!!")
