import lab01

# This function tests your lab 01 code, ensuring that it prints the correct output
def test_main(capsys):
    lab01.main() # run the student's code
    captured = capsys.readouterr()
    assert captured.out == 'Hello, world!' # check if the output is a match
    # assert lab01.hello_world() == "Hello World!"
