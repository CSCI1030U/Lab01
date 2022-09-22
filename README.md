# Lab 01 - Git, GitHub, and GitHub Classroom

In this lab, we'll learn how to use the Git version control system, how to use the GitHub remote repository system, and we'll submit this assignment to invole the auto-grader for these lab assignments by writing and submitting a simple Python program.

_**Note:** The use of an auto-grading system was decided in order to ensure that as much of the lab instructor's time was available for student help as possible.  This lab assignment's primary goal is to familiarize you with the tools required to use GitHub Classroom.  As a bonus, Git, GitHub, and pytest are all tools widely used in industry.  You will use Git and GitHub frequently over the next four years._

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  For this, we will first need to install git.  Use the [instructions on Git's own website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to do this.

The command to make a local close of the repository will look something like this:

```
git clone https://github.com/CSCI1030U/lab01-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

Next we'll install pytest, which is a module for Python that allows you to verify that your code is correct before you submit.

For Linux users, open a terminal and use this command (the MacOS command is similar):

`sudo -H pip3 install pytest`

For Windows users, open an Anaconda Prompt from the start menu and use this command:

`pip install pytest`

If you have previously installed `pytest`, then you can skip this step.


## Instructions

In this lab, you will edit the `lab01.py` file that declares a few variables, and modify the code so that it calculates some new variable values using expressions, and prints the values of those variables.


### Part 1

The variables `cost_per_item` and `quantity` contain numeric values.  Use these two variables to calculate the total cost (before tax) of the items, which calculates the cost of purchasing `quantity` of an item which will cost `cost_per_item` each, putting the value in a new variable called `subtotal_cost`.  Next, calculate the tax on this `subtotal_cost` and put this value into another variable, called `tax`, which will be 13% of the cost (HST).  Finally, assign the sum of these two variables to a new variable, called `total_cost`.


### Part 2

Print the values of all 5 variables, each on their own line, in the form:  `<variable_name> = <variable_value>`.  The exact output of your program will look like this:

```
cost_per_item = $19.99
quantity = 5
subtotal_cost = $99.95
tax = $12.99
total_cost = $112.94
```

To print a number using exactly two decimal places, use `f'variable = {variable:0.2f}'` within your `print()` function call.  One example of this has been included in the `lab01.py` file already, and is also included, below:

```
print(f'cost_per_item = ${cost_per_item:0.2f}')
```


_**Note:** The output has to match exactly, so be sure to put exactly one space on each side of the `=` sign, and there will be a newline after each variable output (as is the default for `print()`)._



## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

`pytest --capture=sys`

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._



## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 01 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
