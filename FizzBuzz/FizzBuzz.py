# The general idea behind this algorithm is to run through a list of numbers and print Fizz when divisible by 3, Buzz when divisible by 5, and FizzBuzz when divisible by both 3 and 5.

def fizzBuzz(list):
    for integer in list:
        if integer % 15 == 0:
            print("FizzBuzz")
        elif integer % 3 == 0:
            print("Fizz")
        elif integer % 5 == 0:
            print("Buzz")
        else:
            print(integer)
