# CPE 101-01
# LAB 7: List Comprehensions
# Name: Keith Lee
# Instructor: S. Einakian
# Section: 7
# Date: 2/22/2022

from Lab7.objects import Circle
from objects import *


# purpose: This function returns a list with the distance from Point(0, 0) to the corresponding Point in the input list.
# signature: list -> list
def point_distance_all(points: list[Point]) -> list[float]:
    distances = [Point.distance(Point(0, 0), point) for point in points]
    return distances


# purpose: This function returns a list of all the Points in the input list that are in the first quadrant
# signature: list -> list
def are_in_first_quadrant(points: list[Point]) -> list[Point]:
    q1_points = [point for point in points if point.x_cord > 0 and point.y_cord > 0]
    return q1_points


# purpose: This function returns a list with all the distances from Point (0, 0) to the corresponding circle in the input list.
# signature: list -> list
def circle_distance_all(circles: list[Circle]) -> list[float]:
    distances = [Point.distance(Point(0, 0), Point(circle.center_cord.x_cord, circle.center_cord.y_cord)) for circle in circles]
    return distances


# purpose: This function returns a list of a Circle objects in the input list that overlap with the Circle at Point (0, 0) with radius 1.
# signature: list -> list
def overlaps_all(circles: list[Circle]) -> list[Circle]:
    overlaps = [circle for circle in circles if Circle.overlaps(Circle(Point(0, 0), 1), circle)]
    return overlaps
