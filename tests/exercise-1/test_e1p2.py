"""
2.	Write a program that will ask the users name, save it in a variable and will then printout 
Hello ____ 
"""

def test_hello_user():
    # capture the input and output of the student's program
    from io import StringIO
    import sys
    sys.stdin = StringIO("Test User\n")
    sys.stdout = StringIO()
    exec(open("exercise-1/e1p2.py").read())
    output = sys.stdout.getvalue().strip()
    
    # assert that the correct output was printed
    assert output == "Hello Test User", f"Expected 'Hello Test User', but got '{output}'"
