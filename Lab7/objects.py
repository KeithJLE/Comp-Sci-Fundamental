# CPE 101-01
# LAB 7: Objects
# Name: Keith Lee
# Instructor: S. Einakian
# Section: 7
# Date: 2/22/2022

from utility import epsilon_equal
from math import sqrt


# This class represents a two-dimensional point with an x and y value.
class Point:
    def __init__(self, x: float, y: float):
        self.x_cord = x
        self.y_cord = y

    def __repr__(self) -> str:
        return "(" + str(self.x_cord) + ", " + str(self.y_cord) + ")"

    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Point and epsilon_equal(self.x_cord, other.x_cord) and epsilon_equal(self.y_cord, other.y_cord)

    # purpose: This function returns the Euclidean distance between the calling Point and the argument Point.
    # signature Point Point -> float
    def distance(self, to) -> float:
        return sqrt((to.x_cord - self.x_cord) ** 2 + (to.y_cord - self.y_cord) ** 2)


# This class represents a circle with the x and y value of its center (this will be an object of the Point class) and a radius value.
class Circle:
    def __init__(self, center: Point, radius: float):
        self.center_cord = center
        self.radius_value = radius

    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Circle and epsilon_equal(self.center_cord.x_cord, other.center_cord.x_cord) and epsilon_equal(self.center_cord.y_cord, other.center_cord.y_cord) and epsilon_equal(self.radius_value, other.radius_value)

    def __ne__(self, other) -> bool:
        return type(self) != type(other) != Circle or not epsilon_equal(self.center_cord.x_cord, other.center_cord.x_cord) or not epsilon_equal(self.center_cord.y_cord, other.center_cord.y_cord) or not epsilon_equal(self.radius_value, other.radius_value)

    def __repr__(self) -> str:
        return str(self.radius_value) + " @ " + str(self.center_cord)

    # purpose: This function returns True when the calling Circle overlaps with the argument Circle and False otherwise. Circles touching at the edge are non-overlapping.
    # signature Circle Circle -> bool
    def overlaps(self, other) -> bool:
        return Point.distance(Point(self.center_cord.x_cord, self.center_cord.y_cord), Point(other.center_cord.x_cord, other.center_cord.y_cord)) < self.radius_value + other.radius_value
