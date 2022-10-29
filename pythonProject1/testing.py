from datetime import datetime
import random
import time
import os

welcome = "Welcome to the ASCII Drag racing game!\n" \
          "Enter your number according to your choice:\n" \
          "1: Start Race\n" \
          "2: Check results of previous rides\n" \
          "3: Exit Game\n"


def clear():
    _ = os.system('clear')


def enjoy_the_ride():
    car_1 = "X"
    car_2 = "O"
    speed = random.randrange(1, 4)
    speed_2 = random.randrange(1, 4)
    track_one = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
    track_two = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
    clear()
    print("X________________|")
    print("O________________|")
    time.sleep(1)
    clear()
    track_one.insert(0, car_1)
    track_two.insert(0, car_2)
    fin_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for ride in range(len(track_one)):
        current_pos = track_one.index(car_1)
        current_pos_2 = track_two.index(car_2)
        next_pos = current_pos + speed
        next_pos_2 = current_pos_2 + speed_2
        track_one.pop(current_pos)
        track_two.pop(current_pos_2)
        track_one.insert(next_pos, car_1)
        track_two.insert(next_pos_2, car_2)
        print(*track_one, sep="")
        print(*track_two, sep="")
        time.sleep(1)
        clear()
        if track_one[17] == "X" and track_two[17] == "|":
            clear()
            print("Car 'X' Won! \nRace Finished!")
            with open("results.txt", "a") as result:
                result.write(f"Car X Won race at {fin_time}\n")
            break
        elif track_two[17] == "O" and track_one[17] == "|":
            clear()
            print("Car 'O' Won! \nRace Finished!")
            with open("results.txt", "a") as result:
                result.write(f"Car O Won race at {fin_time}\n")
            break
        elif car_1 == track_one[17]:
            clear()
            print("TIE!\nRace Finished!")
            with open("results.txt", "a") as result:
                result.write(f"There is a TIE at {fin_time}\n")
                break


while True:
    enjoy = input(welcome)

    if enjoy == "1":
        enjoy_the_ride()
    elif enjoy == "2":
        with open("results.txt", "r") as result:
            print(result.read())
    elif enjoy == "3":
        print("Good bye!\nProgram is Closed")
        quit()
    else:
        print("Incorrect Input")

    want_more = input("Do you want to continue?(yes/no): ")
    if want_more == "yes":
        continue
    elif want_more == "no":
        print("Have a nice day,bye!")
        quit()
    else:
        print("Invalid Input")