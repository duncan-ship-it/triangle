from main import Triangle


def tests():
    points = ["0", "0", "3", "0", "0", "4"]

    triangle = Triangle(points)

    assert triangle.lengths == [3.0, 5.0, 4.0]

    assert triangle.angles == [37, 90, 53]

    assert triangle.type == "Right angle Scalene"

    assert triangle.area == 6


def debug():
    points = ["0", "0", "3", "0", "0", "4"]

    triangle = Triangle(points)

    print(triangle.lengths)


tests()
