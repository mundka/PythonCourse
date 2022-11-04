import car, random, tracks2
from datetime import datetime
from time import sleep

welcome = "Enter your number according to your choice:\n" \
          "1: Start Race\n" \
          "2: Check results of previous rides\n" \
          "3: Exit Game\n"

def start_race():
    user_input = input(f"Start race?: Y\n" 
          "See results?: R")

    if user_input == "Y":
        # define time and format
        fin_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # define track lanes and cars
        lane1 = tracks2.track.lane1
        lane2 = tracks2.track.lane2
        car1 = car.car1.car_model
        car2 = car.car2.car_model
        # insert cars to lanes
        lane1.insert(0, car1)
        lane2.insert(0, car2)
        winner = None

        for ride in range(len(lane1)):
            current_pos1 = lane1.index(car1)
            current_pos2 = lane2.index(car2)
            next_pos1 = current_pos1 + car.car1.speed
            next_pos2 = current_pos2 + car.car2.speed
            lane1.pop(current_pos1)
            lane2.pop(current_pos2)
            lane1.insert(next_pos1, car1)
            lane2.insert(next_pos2, car2)
            print(*lane1)
            print(*lane2)
            sleep(0.2)


            if lane1[len(lane1) - 1] = car1 or lane2[len(lane2) - 1] == car2:
                print(f"race over, winner is {car1}")
                break
            elif lane2[len(lane2) - 1] == car2 and lane1[len(lane1) - 1] == car1:
                print(f"race over, winner is {car2}")




    elif user_input == "R":
        with open("score.csv", "r") as result:
            print(result.read())
    else:
        print("Invalid input")


while True:
    start = input(welcome)

    if start == "1":
        start_race()
    elif start == "2":
        with open("score.csv", "r") as result:
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
        print("Have a nice day, bye!")
        quit()
    else:
        print("Invalid Input")




