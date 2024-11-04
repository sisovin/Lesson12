# Lesson 12: closure

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is closure in Python?

A closure in Python is a function object that has access to variables in its lexical scope, even when the function is called outside that scope. Closures are created by nested functions, where the inner function references variables from the outer function.

Here's an example to illustrate closures:

```python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # This will print "Hello, World!"
```

In this example:

1. `outer_function` defines a variable `msg` and an inner function `inner_function`.
2. `inner_function` references `msg` from its enclosing scope.
3. `outer_function` returns `inner_function`, which is then assigned to `closure`.
4. When `closure` is called, it still has access to `msg` from `outer_function`'s scope, demonstrating a closure.

## What are some practical use cases for closures in Python?

Closures in Python can be used in various practical scenarios. Here are some common use cases:

1. **Data Encapsulation:**
   Closures can be used to encapsulate data and provide controlled access to it.

   ```python
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
   ```

2. **Function Factories:**
   Closures can be used to create functions with pre-configured parameters.

   ```python
   def make_multiplier(factor):
       def multiplier(number):
           return number * factor
       return multiplier

   double = make_multiplier(2)
   triple = make_multiplier(3)

   print(double(5))  # Output: 10
   print(triple(5))  # Output: 15
   ```

3. **Callback Functions:**
   Closures are often used in event handling and callback functions.

   ```python
   def make_callback(message):
       def callback():
           print(message)
       return callback

   hello_callback = make_callback("Hello!")
   goodbye_callback = make_callback("Goodbye!")

   hello_callback()  # Output: Hello!
   goodbye_callback()  # Output: Goodbye!
   ```

4. **Decorators:**
   Closures are the foundation of decorators, which are used to modify the behavior of functions or methods.

   ```python
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
   ```

5. **Maintaining State:**
   Closures can maintain state across function calls without using global variables or class instances.

   ```python
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
   ```

These examples demonstrate how closures can be used to encapsulate data, create configurable functions, handle callbacks, implement decorators, and maintain state.

## What is the difference between a closure and a regular function in Python?

The primary difference between a closure and a regular function in Python lies in how they handle variables from their enclosing scope. Here are the key distinctions:

### Regular Function

- **Scope:** A regular function only has access to its own local variables and the global variables.
- **Lifetime:** Local variables in a regular function are created when the function is called and destroyed when the function exits.
- **Example:**

  ```python
  def regular_function():
      local_var = "I am local"
      print(local_var)

  regular_function()
  ```

### Closure

- **Scope:** A closure has access to variables from its enclosing scope even after the outer function has finished executing.
- **Lifetime:** Variables captured by a closure remain in memory as long as the closure itself is in memory.
- **Example:**

  ```python
  def outer_function(msg):
      def inner_function():
          print(msg)
      return inner_function

  closure = outer_function("Hello, World!")
  closure()  # This will print "Hello, World!"
  ```

### Key Differences

1. **Variable Access:**

   - **Regular Function:** Can only access its own local variables and global variables.
   - **Closure:** Can access variables from its enclosing scope even after the outer function has finished executing.

2. **State Retention:**

   - **Regular Function:** Does not retain state between calls unless using global variables or class attributes.
   - **Closure:** Retains state between calls through the captured variables.

3. **Use Cases:**
   - **Regular Function:** Used for general-purpose tasks where state retention is not required.
   - **Closure:** Useful for scenarios where you need to maintain state or create function factories, decorators, and callbacks.

### Example from the Code

In your provided code, [`parent_function`] creates a closure:

```python
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
```

- **Closure:** The `play_game` function is a closure that captures the `coins` and `person` variables from `parent_function`.
- **State Retention:** Each call to `parent_function` creates a new closure with its own state. The `coins` variable is retained between calls to `sisovin()` and `viphea()`.

This demonstrates how closures can maintain state and access variables from their enclosing scope, which is not possible with regular functions.

**EXPANATIONS:**
Where is the closure? How does the closure works? What are the differences between Closures and the Regular Functions in Python?

we can observe closures in action. Let’s break it down:
**1. Closures:**
**[-]** A closure is a function that “closes over” variables from its enclosing scope, preserving those variables even after the enclosing scope has finished executing.
**[-]** In other words, a closure can access and manipulate variables that are not in its local scope.
**[-]** In Python, closures occur when an inner function (like play_game() in this case) references variables from its outer function (parent_function()).
**[-]** These referenced variables are “captured” by the inner function and remain accessible even after the outer function has completed execution.

**2. How the Closure Works:**

- The **play_game()** function is the inner function within parent_function().
- It references the coins variable from the outer scope (i.e., parent_function()).
- The nonlocal coins statement indicates that coins should be treated as a non-local variable (i.e., it refers to the coins in the enclosing scope).
- When play_game() modifies coins (by decrementing it), it affects the same coins variable declared in parent_function().
- The closure ensures that play_game() retains access to the coins variable even after parent_function() has finished executing.

**3. Differences Between Closures and Regular Functions:**

**[] Scope Access:** - Regular functions can only access variables within their own local scope or global scope. - Closures can access variables from their enclosing (non-global) scope, even after that scope has exited.

**[] Lifetime:** - Regular functions do not retain any state or memory after execution. - Closures “remember” the environment in which they were defined, including variables, and maintain that state beyond their execution.

**[] Use Cases:** - Regular functions are suitable for most tasks where you don’t need to capture external variables. - Closures are useful when you want to create functions with persistent state or when you need to encapsulate behavior along with specific context (e.g., callbacks, decorators).

In the above example code:

- sisovin and viphea are closures because they both reference the coins variable from their respective enclosing scopes (parent_function("Sisovin", 3) and parent_function("Viphea", 5)).
- When you call sisovin(), it decrements the coins value for Sisovin.
- Similarly, when you call viphea(), it modifies the coins value for Viphea.

## What are the advantages of using closures in Python?

Closures in Python offer several advantages, making them a powerful tool for certain programming scenarios. Here are some key benefits:

1. **Data Encapsulation:**

   - Closures allow you to encapsulate data within a function, providing controlled access to that data. This can help in hiding implementation details and protecting the data from external modification.

   ```python
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
   ```

2. **Maintaining State:**

   - Closures can maintain state across function calls without using global variables or class instances. This is useful for creating functions that need to remember previous interactions.

   ```python
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
   ```

3. **Function Factories:**

   - Closures can be used to create functions with pre-configured parameters, allowing for more flexible and reusable code.

   ```python
   def make_multiplier(factor):
       def multiplier(number):
           return number * factor
       return multiplier

   double = make_multiplier(2)
   triple = make_multiplier(3)

   print(double(5))  # Output: 10
   print(triple(5))  # Output: 15
   ```

4. **Callbacks and Event Handlers:**

   - Closures are often used in event-driven programming for defining callbacks and event handlers that need to retain context.

   ```python
   def make_callback(message):
       def callback():
           print(message)
       return callback

   hello_callback = make_callback("Hello!")
   goodbye_callback = make_callback("Goodbye!")

   hello_callback()  # Output: Hello!
   goodbye_callback()  # Output: Goodbye!
   ```

5. **Decorators:**

   - Closures are the foundation of decorators, which are used to modify the behavior of functions or methods in a clean and readable way.

   ```python
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
   ```

6. **Avoiding Global Variables:**

   - Closures help avoid the use of global variables by capturing and retaining the necessary variables within the function's scope.

   ```python
   def outer_function(msg):
       def inner_function():
           print(msg)
       return inner_function

   closure = outer_function("Hello, World!")
   closure()  # Output: Hello, World!
   ```

These advantages make closures a versatile and powerful feature in Python, enabling more modular, maintainable, and reusable code.
