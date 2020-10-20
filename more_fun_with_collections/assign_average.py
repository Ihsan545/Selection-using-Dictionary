"""
Program: assign_average .py
Author: Ihsanullah Anwary
Last date modified: 10/14/2020
This program is an example of case statement using dictionary.
"""


def switch_average(Key):
    """ returns the value of gaven key"""
    grades = {  # declaring dictionary.
        'A': 100,
        'B': 90,
        'C': 80,
        'D': 70,
        'F': 60,
    }
    for grade_key, value in grades.items():
        if grade_key == Key:
            return value


if __name__ == "__main__":
    print(switch_average("B"))
    """" Calling the function to return value"""
