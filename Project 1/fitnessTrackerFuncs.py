# Project 1 Fitness Tracking
#
# Name: Keith Lee
# Section: 7
# Date: 1/18/2022

# purpose: This function prints the welcome message.
# signature: none -> none
def welcome():
    print("Welcome to Fitness Tracker Application!\n\n    To begin you must specify the participant’s name, age. height"
          " (in inches),\n    weight (in lb), exercise duration (in minutes), and exercise type (1-4)!\n    Now you can"
          " compute the burned calories and BMI.")


# purpose: This function asks the user for their name and returns it.
# signature: none -> string
def input_name():
    user_name = input("Enter the name: ")
    return user_name


# purpose: This function asks the user for their age and returns it.
# signature: none -> int
def input_age():
    user_age = int(input("Enter age: "))
    while (user_age <= 0):
        print("Error: age must be an integer > 0!")
        user_age = int(input("Enter age: "))
    return user_age


# purpose: This function asks the user for their height and returns it.
# signature: none -> float
def input_height():
    user_height = float(input("Enter height in inches: "))
    while (user_height <= 0):
        print("Error: height must be greater than 0!")
        user_height = float(input("Enter height in inches: "))
    return user_height


# purpose: This function asks the user for their weight in pounds and returns it.
# signature: none -> float
def input_weight():
    user_weight = float(input("Enter weight in lb: "))
    while (user_weight <= 0):
        print("Error: weight must be greater than 0!")
        user_weight = float(input("Enter weight in lb: "))
    return user_weight


# purpose: This function asks the user for the duration of their exercise in minutes and returns it.
# signature: none -> float
def input_duration():
    user_exercise_duration = float(input("Enter duration of exercise in minutes: "))
    while (user_exercise_duration <= 0):
        print("Error: duration must be greater than 0!")
        user_exercise_duration = float(input("Enter duration of exercise in minutes: "))
    return user_exercise_duration


# purpose: This function asks the user for their exercise type and returns it.
# signature: none -> int
def input_exercise_type():
    exercise_type = int(input("Enter exercise type: 1) low-impact 2) high-impact 3) slow-paced 4) fast-paced "))
    while (exercise_type < 1 or exercise_type > 4):
        print("Error: exercise type must be an integer between [1,4]!")
        exercise_type = int(input("Enter exercise type [1,4]: "))
    return exercise_type


# purpose: This function prints the fitness info of the user.
# signature: string int float float float float float -> none
def print_info(name, age, height, weight, calorie_burned, BMI, miles):
    print("           Name : ", name)
    print("            Age : {0:3d}".format(age))
    print("         Height : {0:6.2f} inches".format(height))
    print("         Weight : {0:6.2f} lb".format(weight))
    print("          Miles : {0:6.2f}".format(miles))
    print("Burned Calories : {0:6.2f}".format(calorie_burned))
    print("            BMI : {0:6.2f}".format(BMI))
    print("   BMI Category :", BMI_category(BMI))


# purpose: This function converts the user's weight in pounds to kilograms and returns it.
# signature: float -> float
def convert_lb_to_kg(weight):
    return weight * 0.45359237


# purpose: This function computes the MET for the user using the exercise type and returns it.
# signature: int -> int
def compute_MET(exercise_type):
    if exercise_type == 1:
        return 5
    elif exercise_type == 2:
        return 7
    elif exercise_type == 3:
        return 3
    elif exercise_type == 4:
        return 4


# purpose: This function computes the amount of calories the user burns by using the duration of their exercise in
# minutes, their weight in kilograms, and their MET value. Then, the function returns that amount of calories burned.
# signature: float float int -> float
def compute_calorie_burned(duration, weight, met_value):
    return duration * met_value * 3.5 * weight / 200


# purpose: This function computes the BMI of the user using their weight in pounds and their height in inches.
# Then, the function returns that BMI value.
# signature: float float -> float
def compute_BMI(weight, height):
    return 703 * weight / (height * height)


# purpose: This function returns the BMI category of the user using their BMI.
# signature: float -> string
def BMI_category(BMI):
    if BMI < 18.59:
        return "Under Weight"
    elif 18.59 <= BMI <= 24.99:
        return "Normal Weight"
    elif 25 <= BMI <= 29.99:
        return "Over Weight"
    else:
        return "Obesity"


# purpose: This function returns the steps per minute of the user using the MET value.
# signature: int -> int
def compute_exercise_type_steps(met_value):
    if met_value == 5:
        return 120
    elif met_value == 7:
        return 227
    elif met_value == 3:
        return 100
    elif met_value == 4:
        return 152


# purpose: This function computes the amount of miles the user will complete by taking into account their height in
# inches, the amount of steps they will take per minute using their exercise type, and the duration of their exercise
# in minutes. Then, the function returns that amount of miles.
# signature: float int float -> float
def compute_equivalent_miles(height, exercise_type_steps, duration):
    feet_per_step = (0.413 * height) / 12
    return feet_per_step * duration * exercise_type_steps / 5280

