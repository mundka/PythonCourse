import game, car

class Outcome:
    def __int__(self, winner, loser, tie):
        self.winner = winner
        self.loser = loser
        self.tie = tie

    def race_end(self):
        if self.winner == car.car1 or car.car2:
            results = f"\nWinner is {self.winner} and {self.loser} lost\n"
            return results
        else:
            results = f"\nIt's a TIE"
            return results

    def save_game(self):
        with open("score.csv", "w") as f:
            f.write((self.race_end()))
