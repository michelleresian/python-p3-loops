#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while (i >= 1):
        print(i)
        i -= 1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    squares_list = [int ** 2 for int in int_list]
    # print(squares_list)
    return squares_list
square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print ("FizzBuzz")
        elif number % 3 == 0:
            print ("Fizz")
        elif number % 5 == 0:
            print ("Buzz")
        else:
            print (number)
fizzbuzz()