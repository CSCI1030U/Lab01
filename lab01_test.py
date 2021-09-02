import lab01
import sys

# This function tests your lab 01 code, ensuring that it prints the correct output
def test_main(capsys):
    lab01.main() # run the student's code
    captured = capsys.readouterr()
    sys.stderr.write('actual output:\n')
    sys.stderr.write(captured.out + '\n')
    correct_output = 'cost_per_item = $19.99\nquantity = 5\nsubtotal_cost = $99.95\ntax = $12.99\ntotal_cost = $112.94\n'

    sys.stderr.write('correct output:\n')
    sys.stderr.write(correct_output + '\n')
    assert captured.out == correct_output # verify that the output is a match
