# [ ] create, call and test the str_analysis() function  

# Tests input from user
def str_analysis(input_string):
    if input_string.isdigit(): # If input only includes numeric values.
        input_string = int(input_string) # Converts str to int

        if input_string > 99: # Greater than 99
            return str(input_string) + " is a big number."
        else:# Less than than 99
            return str(input_string) + " is a small number."
    else: # If input is not a digit
        if input_string.isalpha(): # Only alphabetic characters
            return input_string + " uses only alphabetic characters."
        else: # Multiple character types
            return input_string + " uses multiple character types."

print("Welcome to StringTester.\n-------------------------") # Program title

while True:
    user_input = input("Input string for testing: ") # Gets input from user.
    if user_input == "": # If no data is entered.
        print("No input detected.")
    else: # If input has data (ready for testing)
        print(str_analysis(user_input)) # Sends input for testings
        break
