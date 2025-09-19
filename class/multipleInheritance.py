class Wheel:
    def wheel_info(self):
        print("Wheel: Used for support and rotation.")

class Rubber:
    def rubber_info(self):
        print("Rubber: Provides grip and cushioning.")

class Tyre(Wheel, Rubber):
    def tyre_info(self):
        print("Tyre: Combination of Wheel and Rubber.")


t = Tyre()
t.wheel_info()
t.rubber_info()
t.tyre_info()
