from main import Triangle


def tests():
    points = ["0", "0", "3", "0", "0", "4"]

    triangle = Triangle(points)

    assert triangle.lengths == [3, 4, 5]

    assert triangle.angles == [37, 53, 90]

    assert triangle.type == "Right angle Scalene"

    assert triangle.area == 6


tests()

