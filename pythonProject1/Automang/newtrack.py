import time, sys, car
from time import sleep
class Tracks:

    def progress_bar1(track):
        trackLength = 30 # Modify this to change the length of the progress bar
        #status = ""
        if isinstance(track, int):
           track = float(track)
        if not isinstance(track, float):
            track = 0
            status = "error: progress must be float\r\n"
        if track < 0:
            track = 0
            status = "Halt...\r\n"
        if track >= 1:
            track = 1
            status = "Done...\r\n"
        block1 = int(round(trackLength * track))
        text1 = "Ferrari: [{0}] ".format(">" * block1 + "_" * (trackLength - block1), track * 100)
        sys.stdout.write(text1) and (text1)
        sys.stdout.flush()

    def progress_bar2(track):
        trackLength = 30 # Modify this to change the length of the progress bar
        #status = ""
        if isinstance(track, int):
           track = float(track)
        if not isinstance(track, float):
            track = 0
            status = "error: progress must be float\r\n"
        if track < 0:
            track = 0
            status = "Halt...\r\n"
        if track >= 1:
            track = 1
            status = "Done...\r\n"
        block1 = int(round(trackLength * track))
        text1 = "\rPorsche: [{0}] ".format(">" * block1 + "_" * (trackLength - block1), track * 100)
        sys.stdout.write(text1)
        sys.stdout.flush()

    print("RACE: ")
    for i in range(101):
        sleep(Car_game_car.car1.speed)
        progress_bar1(i / 100.0)
        sleep(Car_game_car.car2.speed)
        progress_bar2(i / 100.0)