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

fizz_buzz(100)