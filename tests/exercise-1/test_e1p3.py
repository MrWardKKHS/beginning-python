"""
3.	Write a program that will ask the user for a number, save it in a variable called num and will then print out the following information using that number, with each statement on a different line.

The number is ___
5 times ____ is _____
if you add 3 to ____ the answer is _____
if you divide 20 by _____ the answer is ______

You may add some other calculations of your own.

"""

def test_number_info():
    # capture the input and output of the student's program
    from io import StringIO
    import sys
    sys.stdin = StringIO("10\n")
    sys.stdout = StringIO()
    exec(open("exercise-1/e1p3.py").read())
    output = sys.stdout.getvalue().strip()
    
    # split the output into lines
    lines = output.split("\n")
    
    # assert that there are at least 4 lines in the output
    assert len(lines) >= 4, f"Expected at least 4 lines, but got {len(lines)}"
    
    # assert that each line contains the expected string
    assert "The number is 10" in lines[0], "Expected 'The number is 10' on first line"
    assert "5 times 10 is 50" in lines[1], "Expected '5 times 10 is 50' on second line"
    assert "if you add 3 to 10 the answer is 13" in lines[2], "Expected 'if you add 3 to 10 the answer is 13' on third line"
    assert "if you divide 20 by 10 the answer is 2" in lines[3], "Expected 'if you divide 20 by 10 the answer is 2' on fourth line"
