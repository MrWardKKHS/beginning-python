"""
1.	Wrie a program that will print out your name, address and telephone number each on a separate line.
"""

from io import StringIO
import sys

def test_name_address_telephone():
    # capture the output of the student's program
    sys.stdout = StringIO()
    exec(open("exercise-1/e1p1.py").read())
    output = sys.stdout.getvalue().strip()

    # split the output into lines
    lines = output.split("\n")

    # assert that there are exactly 3 lines in the output
    assert len(lines) == 3, f"Expected 3 lines, but got {len(lines)}"

    # assert that each line contains the expected string
    assert "Name:" in lines[0], "Expected 'Name:' on first line"
    assert "Address:" in lines[1], "Expected 'Address:' on second line"
    assert "Phone:" in lines[2], "Expected 'Telephone:' on third line"
