'''
Mystery Number
Pawelski
1/27/2025

Instructions:
1.  Before running the program, predict what it will
    do. Check your prediction by running the program
    and entering a variety of values.
2.  Currently, the program does not display anything
    when you don't guess the mystery number. Add an
    else statement to the program so that the message
    "You didn't guess my mystery number. It was 36!"
    gets displayed to the shell.
3.  Modify the program by changing the mystery number.
    When you didn't guess the new mystery number, did
    the print display the correct number? If not, how
    could you modify the print so that it displays the
    correct mystery number in all circumstances?
'''

mystery_number = 36
guess = int(input("Guess my mystery number (1-100) >> "))
if guess == mystery_number:
    print("You guessed my mystery number!")
# Add your code here!