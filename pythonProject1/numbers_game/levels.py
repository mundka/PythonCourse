import random

class Levels:
    def game_range(self):
        pass


level1 = Levels
level1.vahemik = random.randint(1, 3)

level2 = Levels
level2.vahemik2 = random.randint(1, 5)

level3 = Levels
level3.vahemik3 = random.randint(1, 10)
#
range1 = level1.vahemik
range2 = level2.vahemik2
range3 = level3.vahemik3

#print(level1.vahemik)
#print(level2.vahemik2)
#print(level3.vahemik3)
