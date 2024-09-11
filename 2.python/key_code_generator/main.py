import math
import random

# Function to calculate the distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to calculate finger travel for a given 6-digit number
def calculate_finger_travel(number):
    keypad = {
        '1': (0, 0), '2': (1, 0), '3': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '7': (0, 2), '8': (1, 2), '9': (2, 2),
        '0': (1, 3)
    }

    total_distance = 0
    number_str = str(number)
    for i in range(len(number_str) - 1):
        total_distance += distance(keypad[number_str[i]], keypad[number_str[i + 1]])

    return total_distance

# Function to check if a number meets the specified criteria
def meets_criteria(number):
    number_str = str(number)
    
    # Check for repeated digits in a 6-digit number
    if len(set(number_str)) != 6:
        return False
    
    return True

# Generate 6-digit numbers that meet the criteria
results = []
while len(results) < 10:
    number = random.randint(100000, 999999)
    if meets_criteria(number):
        finger_travel = calculate_finger_travel(number)
        if 10 < finger_travel < 12:
            results.append((number, finger_travel))

# Sort the results by finger travel in decreasing order
results.sort(key=lambda x: x[1], reverse=True)

# Print the results in a table format
print("{:<15} {:<15}".format("6-Digit Number", "Finger-Travel"))
for number, finger_travel in results:
    print("{:<15} {:<15.2f}".format(number, finger_travel))
