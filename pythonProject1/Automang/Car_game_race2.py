import car, time, newtrack


welcome = "Enter your number according to your choice:\n" \
          "1: Start Race\n" \
          "2: Check results of previous rides\n" \
          "3: Exit Game\n"

while True:
    start = input(welcome)

    if start == "1":
        print("Start race?: Y", "Quit: Q")
        input1 = str(input())
        input1 = input1.upper()

        if input1 == "Q":
            break
        elif input1 == "Y":

            print("RACE: ")
            for i in range(101):
                time.sleep(Car_game_car.car1.speed)
                newtrack.Tracks.progress_bar1(i / 100.0)
                time.sleep(Car_game_car.car2.speed)
                newtrack.Tracks.progress_bar2(i / 100.0)


    elif start == "2":
        with open("scoreboard.txt", "r") as result:
            print(result.read())
    elif start == "3":
        print("Good bye!\nProgram is Closed")
        quit()
    else:
        print("Incorrect Input")

# want_more = input("Do you want to continue?(yes/no): ")
# if want_more == "y":
#     continue
# elif want_more == "n":
#     print("Have a nice day,bye!")
#     quit()
# else:
#   print("Invalid Input")