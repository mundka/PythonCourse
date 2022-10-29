if lane1[len(lane1) - 1] == "|":
    winner = car1
elif lane2[len(lane2) - 1] == "|":
    winner = car2
elif lane1[len(lane1) - 1] == "|" and lane2[len(lane2) - 1] == "|":
    winner = "TIE"
    if winner == "TIE":
        print("TIE! \nRace over")
        with open("score.csv", "a") as result:
            result.write(f"It's a TIE at {fin_time}\n")
            break
    print(f"{winner} won \n Race over")
    with open("score.csv", "a") as result:
        result.write(f"{winner} won race at {fin_time}\n")
        break