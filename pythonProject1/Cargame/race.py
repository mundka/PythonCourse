
class Race:
    def __int__(self, track, car1, car1_speed, car2, car2_speed):
        self.track = track
        self.car1 = car1
        self.car1_speed = car1_speed
        self.car2 = car2
        self.car2_speed = car2_speed

    def race_func(self):
        track1 = self.track.copy()
        track2 = self.track

        print(track1)