# FizzBuzz
# Input: Number to generate fizzbuzz to
# Output: None. Prints to console directly
def fizz_buzz(x):
    fb = lambda n, m : n % m
    for i in range(x + 1):
        if fb(i, 15) == 0:
            print("FizzBuzz")
        elif fb(i, 5) == 0:
            print("Buzz")
        elif fb(i, 3) == 0:
            print("Fizz")
        else:
            print(i)

# Palendrome
# Input: A single word as string
# Output: Boolean representing whether or not the word is a palendrome
def palendrome(word):
    reverse = word[::-1]
    if reverse == word:
        return True
    else:
        return False

# Word Count
# Input: a string
# Output: Number of words in string
def word_count(text):
    count = 1
    for c in text:
        if c == ' ':
            count += 1
    return count


# INPUT FUNCTIONS

# Get Help
# Lists all commands that are available for the user
def get_help():
    commands = {
        'fizzbuzz' : 'Initiate the fizz buzz module',
        'fizz' : 'Initiate the fizz buzz module. Alias for fizzbuzz',
        'help' : 'Print off a list of commands',
        'h' : 'Print off a list of commands. Alias for help',
        'quit' : 'Terminates the program',
        'q' : 'Terminates the program. Alias for quit'
    }
    print()
    for key in commands:
        print(key + ': ' + commands[key])
    print()