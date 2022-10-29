import car
from time import sleep


track1 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
track2 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]

position = 0
index = 0
index2 = 0
asfalt = position + 1

while index <= 10:
    if index == 10:
        print("you won")
        break
    else:
        track1.pop(index)
        track1.insert(position, Car_game_car.car1.car_model)
        #track2.pop(index)
        #track2.insert(position, Car_game_car.car2.car_model)

        if index > 0:
            track1.insert(asfalt, "_")
           # track2.insert(asfalt, "_")
            track1.pop(index2)
           # track2.pop(index2)

            sleep(Car_game_car.car1.speed)
           # sleep(Car_game_car.car2.speed)
        print(track1)
       # print(track2)
    index += 1