# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
# Closure is a function having access to the scope of its parent
# function after the parent function has returned.
from turtle import title

print("")
title = " Lesson 12: Closure "
print(f"{title}".center(80, "="))
print("")

def parent_function(person, coins):
  coins = 3
  
  def play_game():
    nonlocal coins
    coins -= 1
    
    if coins > 1:
      print("\n" + person + " has " + str(coins) + " coins left")
    elif coins == 1:
      print("\n" + person + " has " + str(coins) + " coin left")
    else:
      print("\n" + person + " is out of coins")
      
  return play_game
    
    
sisovin = parent_function("Sisovin", 3)
viphea = parent_function("Viphea", 5)

sisovin()
sisovin()

viphea()

sisovin()
print("")
# %%
title = " The illustrated closures "
print(f"{title}".center(80, "="))
#  The illustrated closures:

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # This will print "Hello, World!"
# %%
title = " to encapsulate data and provide controlled access to it "
print(f"{title}".center(80, "="))
# to encapsulate data and provide controlled access to it.
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
# %%
title = " to create a function factory "
print(f"{title}".center(80, "="))
# to create a function factory.
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
# %%
title = " Closures in event handling and callback functions. "
print(f"{title}".center(80, "="))
# Closures in event handling and callback functions.
def make_callback(message):
    def callback():
        print(message)
    return callback

hello_callback = make_callback("Hello!")
goodbye_callback = make_callback("Goodbye!")

hello_callback()  # Output: Hello!
goodbye_callback()  # Output: Goodbye!
# %%
title = " Create Decorators using Closures "
print(f"{title}".center(80, "="))
# Create Decorators using Closures
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
# %%
title = " Closures on Maintaining State "
print(f"{title}".center(80, "="))
# Closures on Maintaining State
def make_accumulator():
    total = 0
    def accumulator(value):
        nonlocal total
        total += value
        return total
    return accumulator

acc = make_accumulator()
print(acc(10))  # Output: 10
print(acc(20))  # Output: 30

title = " Example on Regular Function "
print(f"{title}".center(80, "="))
# Example on Regular Function
def regular_function():
    local_var = "I am local"
    print(local_var)

regular_function()

title = " Example on Closure "
print(f"{title}".center(80, "="))
# Example on Closure
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # This will print "Hello, World!"
# %%
title = " Closure with Avoiding Global Variables "
print(f"{title}".center(80, "="))
# Closure with Avoiding Global Variables
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # Output: Hello, World!
# %%
