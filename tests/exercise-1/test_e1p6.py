"""
6.	Write a program which will ask for three numbers, save them in three different variables and will then print out the three numbers, the total and the average in the following format:

The numbers were ___, ____ and _____
The total of these numbers is ___________
The average of these numbers is _____________


"""

def test_average_of_three_numbers():
    # capture the input and output of the student's program
    from io import StringIO
    import sys
    sys.stdin = StringIO("10\n20\n30\n")
    sys.stdout = StringIO()
    exec(open("exercise-1/e1p6.py").read())
    output = sys.stdout.getvalue().strip()
    
    # split the output into lines
    lines = output.split("\n")
    
    # assert that there are at least 3 lines in the output
    assert len(lines) >= 3, f"Expected at least 3 lines, but got {len(lines)}"
    
    # assert that each line contains the expected string
    assert "The numbers were 10, 20 and 30" in lines[0], "Expected 'The numbers were 10, 20 and 30' on first line"
    assert "The total of these numbers is 60" in lines[1], "Expected 'The total of these numbers is 60' on second line"
    assert "The average of these numbers is 20.0" in lines[2], "Expected 'The average of these numbers is 20.0' on third line"
