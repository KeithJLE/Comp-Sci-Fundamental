# Main Program
# Project 1 Fitness Tracking
#
# Name: Your Name
# Section: Your Section
# Date:
from fitnessTrackerFuncs import *


def main():
    welcome()
    fitness_tracker()


# purpose: This function runs the code for the fitness tracker, excluding the welcome message.
# signature: none -> none
def fitness_tracker():
    name = input_name()
    age = input_age()
    height = input_height()
    weight_in_lb = input_weight()
    weight_in_kg = convert_lb_to_kg(weight_in_lb)
    duration = input_duration()
    exercise_type = input_exercise_type()
    met_value = compute_MET(exercise_type)
    exercise_type_steps = compute_exercise_type_steps(met_value)
    BMI = compute_BMI(weight_in_lb, height)
    calorie_burned = compute_calorie_burned(duration, weight_in_kg, met_value)
    miles = compute_equivalent_miles(height, exercise_type_steps, duration)
    print_info(name, age, height, weight_in_lb, calorie_burned, BMI, miles)
    restart()


# purpose: This function asks the user if they want to apply fitness tracking for another user and then reruns the
# fitness tracker or ends it depending on their answer
# signature: none -> none
def restart():
    answer = input("Do you want to apply fitness tracking for another user (y/n)?\n")
    while (answer != "y" and answer != "n"):
        answer = input("Do you want to apply fitness tracking for another user (y/n)?\n")
    if answer == "y":
        fitness_tracker()
    elif answer == "n":
        return


if __name__ == '__main__':
    main()
