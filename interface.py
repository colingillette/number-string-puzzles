# List Reader
# Input: List
# Output: none, but will print list to console one line at a time
def list_reader(x):
    for i in range(len(x)):
        print(x[i])

# Fibonacci Sequence
# Input: Number in return series
# Output: List in series
def fib(x):
    if x < 1:
        return False
    elif x == 1:
        return [0]
    elif x == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, x):
        seq.append(seq[i-1] + seq[i-2])

    return seq

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
        'q' : 'Terminates the program. Alias for quit',
        'fibonacci' : 'Initate the fibonacci sequence module',
        'fib' : 'Initate the fibonacci sequence module. Alias for fibonacci'
    }
    print()
    for key in commands:
        print(key + ': ' + commands[key])
    print()

# Process Input
# Input: string from user
# Output: Boolean. Will always be true unless user types 'quit' or 'q'
def process_input(text):
    status = True
    text = text.lower()
    if text == 'quit' or text == 'q':
        print('Exiting program...')
        status = False
    elif text =='fizz' or text == 'fizzbuzz':
        fizz_buzz(int(input('Enter the number you would like to go to: ')))
    elif text == 'help':
        get_help()
    elif text == 'fib' or text == 'fibonacci':
        list_reader(fib(int(input('How many numbers would you like to generate: '))))
    else:
        print('Please input a valid command. Type \"help\" if you need a list of commands.')
    return status

# Computer
# A function that handles input from the user
def computer():
    print()
    print("For a list of commands, please type \"help\"")
    print()
    live = True
    while (live):
        task = str(input('Please enter a command: '))
        live = process_input(task)
    
    

# MAIN BODY
computer()