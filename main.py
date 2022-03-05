import csv
import matplotlib.pyplot as plt

from math import acos, ceil, degrees, dist, sqrt
from numpy import prod


class Triangle:
    def __init__(self, points):
        # organise list of points into 3 tuples of (x, y) float coordinates
        self.points = self.p1, self.p2, self.p3 = [tuple(map(float, points[i*2:i*2+2])) for i in range(3)]

        self.lengths = [dist(self.p1, self.p2),
                        dist(self.p1, self.p3),
                        dist(self.p2, self.p3)]

        self.angles = [self.get_angle(i) for i in range(3)]

        self.area = self.get_area()

        self.type = self.get_type()  # determine type of triangle from angles and side lengths

    def __str__(self):
        return str(self.points)  # helpful for debug

    # use Heron's formula to find area using side lengths
    def get_area(self, precision=3):
        s = sum(self.lengths)/2

        return round(sqrt(s*prod([s - side for side in self.lengths])), precision)

    def perimeter(self, precision=3):
        # sum the distances between each point
        return round(sum(self.lengths), precision)

    # get angle around point p
    def get_angle(self, p):
        a = self.lengths[p]
        b, c = self.lengths[:p] + self.lengths[p+1:]  # unpack other two lengths as b and c

        return int(round(degrees(acos((a**2 - b**2 - c**2)/(-2 * b * c))), 0))

    # determine type of triangle from side lengths and angles
    def get_type(self):
        if self.area == 0:
            return "Degenerate"

        unique_lengths = len(set(self.lengths))

        if unique_lengths == 1:
            return "Equilateral"
        elif unique_lengths == 2:
            tri_type = "Isosceles"
        else:
            tri_type = "Scalene"

        angle_type = "Acute"  # assume acute triangle

        for angle in self.angles:
            if angle == 90:
                angle_type = "Right angle"
                break
            elif angle > 90:
                angle_type = "Obtuse"
                break

        return f"{angle_type} {tri_type}"

    def plot(self, ax):
        x, y = zip(*self.points + [self.points[0]])  # append first point to close polygon shape

        ax.fill(x, y)  # shade in triangle

        # describe properties of triangle
        ax.text(min(x),
                min(y),
                f"Perimeter: {self.perimeter()}\nSA: {self.area}\nType: {self.type}\n")


def get_triangles():
    reader = csv.reader(open("triangles.csv", "r"))

    for points in reader:
        try:
            yield Triangle(points)
        except ValueError:
            print(f"[ERROR] Could not parse triangle from {points}")


def main():
    triangles = list(get_triangles())

    rows, cols = 2, ceil(len(triangles)/2)

    fig, ax = plt.subplots(nrows=rows, ncols=cols)

    for r_c, row in enumerate(ax):
        for c_c, col in enumerate(row):
            try:
                triangles[cols*r_c + c_c].plot(col)
            except IndexError:
                break  # list of triangles exhausted

    plt.show()  # display graph


if __name__ == "__main__":
    main()
