import car, random
from datetime import datetime
from time import sleep
welcome = "Enter your number according to your choice:\n" \
          "1: Start Race\n" \
          "2: Check results of previous rides\n" \
          "3: Exit Game\n"


def race():
    track1 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
    track2 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
    fin_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    car1 = car.car1.car_model
    car2 = car.car2.car_model
    speed1 = random.randrange(1, 4) + car.car1.speed
    speed2 = random.randrange(1, 4) + car.car2.speed

    track1.insert(0, car1)
    track2.insert(0, car2)

    for ride in range(len(track1)):
        current_pos1 = track1.index(car1)
        current_pos2 = track2.index(car2)
        next_pos1 = current_pos1 + speed1
        next_pos2 = current_pos2 + speed2
        track1.pop(current_pos1)
        track2.pop(current_pos2)
        track1.insert(next_pos1, car1)
        track2.insert(next_pos2, car2)
        print(*track1)
        print(*track2)
        sleep(0.5)

        if track1[19] == car.car1.car_model and track2[19] == "|":

            print("Ferrari won \n Race over")
            with open("scoreboard.txt", "a") as result:
                result.write(f"Ferrari won race at {fin_time}\n")
            break
        elif track2[19] == car.car2.car_model and track1[19] == "|":

            print("Porsche won \n Race over")
            with open("scoreboard.txt", "a") as result:
                result.write(f"Porsche won race at {fin_time}\n")
            break
        elif car1 == track1[19]:

            print("TIE! \nRace over")
            with open("scoreboard.txt", "a") as result:
                result.write(f"It's a TIE at {fin_time}\n")
                break


while True:
    start = input(welcome)

    if start == "1":
        race()
    elif start == "2":
        with open("scoreboard.txt", "r") as result:
            print(result.read())
    elif start == "3":
        print("Good bye!\nProgram is Closed")
        quit()
    else:
        print("Incorrect Input")

    want_more = input("Do you want to continue?(yes/no): ")
    if want_more == "y":
        continue
    elif want_more == "n":
        print("Have a nice day,bye!")
        quit()
    else:
        print("Invalid Input")
