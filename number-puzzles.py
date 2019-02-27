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
    for i in range(2, x + 1):
        seq.append(seq[i-1] + seq[i-2])

    return seq



# MAIN BODY

list_reader(fib(10))