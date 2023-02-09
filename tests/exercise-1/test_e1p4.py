"""
4.	Write a program that will ask for a particular number of inches and will convert that number to cm, with an output like

______ inches is equal to _______ cm

(1 inch = 2.54 cm)

"""

def test_inches_to_cm():
    # capture the input and output of the student's program
    from io import StringIO
    import sys
    sys.stdin = StringIO("10\n")
    sys.stdout = StringIO()
    exec(open("exercise-1/e1p4.py").read())
    output = sys.stdout.getvalue().strip()
    
    # assert that the correct output was printed
    assert output == "10 inches is equal to 25.4 cm", f"Expected '10 inches is equal to 25.4 cm', but got '{output}'"
