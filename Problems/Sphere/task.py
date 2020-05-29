class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.volume = 4.0 / 3.0 * float(Sphere.PI) * pow(radius, 3)
