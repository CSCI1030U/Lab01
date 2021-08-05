import lab01

# This function tests your lab 01 code, ensuring that it prints the correct output
def test_main(capsys):
    captured = capsys.readouterr()
    assert captured.out == 'Hello, world!'
    # assert lab01.hello_world() == "Hello World!"
