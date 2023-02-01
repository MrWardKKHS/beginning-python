def test_name_address_telephone():
    # capture the output of the student's program
    from io import StringIO
    import sys
    sys.stdout = StringIO()
    exec(open("1_1.py").read())
    output = sys.stdout.getvalue().strip()
    
    # split the output into lines
    lines = output.split("\n")
    
    # assert that there are exactly 2 lines in the output
    assert len(lines) == 2, f"Expected 3 lines, but got {len(lines)}"
    
    # assert that each line contains the expected string
    assert "Name:" in lines[-1], "Expected 'Name:' on first line"
    assert "Address:" in lines[0], "Expected 'Address:' on second line"
    assert "phone:" in lines[1], "Expected 'phone:' on third line"
