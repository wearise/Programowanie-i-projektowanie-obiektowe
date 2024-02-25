class Speed:
    def __init__(self, factor):
        self._starting_speed = factor // 6
        self._speed = factor // 6
        self._new_speed = factor // 6

    @property
    def starting_speed(self):
        return self._starting_speed

    @property
    def speed(self):
        return self._speed

    # @speed.setter
    # def speed(self,):
    #     self._speed

    def register_new_speed(self, new_speed):
        self._new_speed = new_speed

    def update_speed(self):
        self._speed = self._new_speed

    def reset_speed(self):
        self._new_speed = self._starting_speed