import sys
sys.path.append("the_programs")
userinput = input("""which system do you want to use?
1.number guessing with the computer
2.fibonacci sequence
3.mulltiplication table
insert your choice:""")
if int(userinput)== 1:
    import four_digits_list
if int(userinput)== 2:
    import Fibonacci_sequence
if int(userinput)== 3:
    import multiplication_table