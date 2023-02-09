"""
5.	Write a program that will ask the user’s age and then outputs a statement saying

Your current age is _________
In the year 2020 you will be ______ years old

"""

import datetime

def test_age_in_2050():
    # capture the input and output of the student's program
    from io import StringIO
    import sys
    sys.stdin = StringIO("30\n")
    sys.stdout = StringIO()
    exec(open("exercise-1/e1p5.py").read())
    output = sys.stdout.getvalue().strip()
    
    # split the output into lines
    lines = output.split("\n")
    
    # assert that there are at least 2 lines in the output
    assert len(lines) >= 2, f"Expected at least 2 lines, but got {len(lines)}"
    
    # calculate the expected age in 2050
    current_year = datetime.datetime.now().year
    current_age = 30
    expected_age_in_2050 = current_age + (2050 - current_year)
    
    # assert that each line contains the expected string
    assert f"Your current age is 30" in lines[0], "Expected 'Your current age is 30' on first line"
    assert f"In the year 2050 you will be {expected_age_in_2050} years old" in lines[1], f"Expected 'In the year 2050 you will be {expected_age_in_2050} years old' on second line"
