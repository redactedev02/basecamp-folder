# Python 03: Iterative Programs — werkblad

> Vragen uit [week 3 voorbereiding.md](./week%203%20voorbereiding.md). Vul je antwoord onder elke vraag in.

---

## Step-01: Strings

#### 7. What are the functionality of functions: _len()_, _split()_, _join()_, _replace()_. Try two examples for each function in Python shell.

len() calculates the length of a string
split() functie splits a string into a list. string.function(arguments)
join(we can combine it again using) string.join(arguments)
replace vervangt iets uit de string.

### Exercises

#### Oefening 2. Ask the user to input a text. Replace the first character with a `k` and print the result.

```python
new_input = user_input.replace(user_input[0], "k", 1)
```

#### Oefening 3. Make a variable with the text "this is a text". Remove all spaces from it. Print the result.

```python
user_input = "this is a text"

new_input = user_input.replace(" ", "")
print(f"New input: {new_input}")
```

#### Oefening 4. Ask the user to input a text. Capitalize the complete input. Print the result.

```python
user_input = "this is a text"

new_input = user_input.upper()
print(f"New input: {new_input}")
```

#### Oefening 6. Ask the user to input a text. Count how many times the input contains the character `i`. Print the result.

```python
user_input = input("zeg iets: ")
amount = user_input.count("i")
print(f"New input: {amount}")
```

---

## Step-02: Looping with _while_

### What to Learn

#### 2. Using _while_ loop implement a program that prints a message (like _Hello_) for 10 times.

```python
amount = 0
while amount <= 10:
    amount += 1
    print("Hello")
```

#### 3. Using _while_ loop implement a counter that counts down from 10 until 0. In each iteration, the program must print the value of the counter.

```python
amount = 10
while amount > 0:
    if amount == 10:
        print(amount)
        amount -= 1
    else:
        amount -= 1
        print(amount)
```

#### 4. What is _break_ statement?

a break statement can be executed to exit a while lope if a condition is met with for example an if statement

#### 5. Implement a program that repeatedly asks the user to enter a character as input until the user enters _q_. If the user enters _q_ the program will stop.

```python
while True:
    value = input("Say something, or say quit to exit:")
    if value == "quit":
        print("Stopped the loop")
        break
    print(value)
```

### Exercises

#### Oefening 1. Print the numbers 1 to 42 using a `while` loop.

```python
value = 0
while value <= 42:
    print(value)
    value += 1
```

#### Oefening 2. Print all odd numbers between 1 to 100 by using a `while` loop.

```python
amount = 100
while amount <= 100 and amount != 0:
    if amount % 2 == 0:
        amount -= 1

    else:
        print(f"This is an odd number, {amount}")
        amount -= 1
```

#### Oefening 3. Print the numbers from 10 to -10 using a `while` loop.

```python
amount = 10
while amount <= 10 and amount != -11:
    print(f"{amount}")
    amount -= 1
```

#### Oefening 4. Ask the user to input a text. Print each character of the input on a new line using a `while` loop.

```python
user_input = input("Give an input:")

# Processing
user_input_length = len(user_input)
process_progress = 0
position = 0

while process_progress < user_input_length:
    print(user_input[position])
    process_progress += 1
    position += 1
```

Verbeterd:

```python
user_input = input("Give an input: ")

position = 0
while position < len(user_input):
    print(user_input[position])
    position += 1
```

#### Oefening 5. Ask the user to input a text. Print each character of the input that is the character `e` or `a` on a separate line.

```python
user_input = input("Give an input: ")

# Processing
position = 0
while position < len(user_input):
    if user_input[position] == "e" or user_input[position] == "a":
        print(f"{user_input[position]}")
position += 1
```

---

## Step-03: Looping with _for ... in_

### What to Learn

#### 1. What are the main elements of a _for_ loop?

repeat something for a certain amount of times

#### 2. Using _for_ loop implement a program that prints a message (like _Hello_) for 10 times.

```python
for count in range(10):
    print("Hello")
```

#### 3. Using _for_ loop implement a counter that counts down from 10 until 0. In each iteration, the program must print the value of the counter.

```python
number = 10
for count in range(11):
    print(f"{number}")
    number -= 1
```

#### 4. Can you use a _break_ statement within a _for_ loop? Build a simple example.

```python
number = 10
for count in range(20):
    print(f"{number}")
    number -= 1
    if number == -3:
        break
```

#### 5. Implement a _for_ loop that prints characters of a given string.

#### 6. Implement a _for_ loop that given a string, prints characters positioned in odd indeces, i.e. `1,3,5,7,...`.

### Exercises

#### Oefening 1. Print the numbers 1 to 42 using a `for` loop.

#### Oefening 2. Print all uneven numbers between 1 to 100 by using a `for` loop.

#### Oefening 3. Ask the user to input a text. Print each character of the input on a new line using a `for` loop.

#### Oefening 4. The `for` and `while` are considered 'loops'. Explain in your own words what a loop is.

#### Oefening 5. Describe the difference between the `for` and `while` in your own words.

#### Oefening 6. Practice the exercises listed in **BRef-01-Chapter 06: Things to Do**

- **6.1**, **6.2** and **6.3**.

---

## Code Analysis

#### Opdracht 1. For each of the following given codes

- Without executing the code try to read the code and write down what will be the output.
  - Use the [Python Code Visualizer](https://cscircles.cemc.uwaterloo.ca/visualize) and execute the code step-by-step. Observe how the variables and statements are executing in each iteration of the loops.

```python
# Code 1
i = 7
for number in range(1, i + i):
	print(number)
```

```python
# Code 2
i = 1
j = 10
for number in range(i, j):
   if number > 5:
       print(number)
   else:
       print('Hello')
```

```python
# Code 3
sentence = "I just came to say hello!"
count = 0
for letter in sentence:
   if letter == " ":
       count = count + 1
   elif letter == "a":
       count = count - 1
print(count)
```

```python
# Code 4
sentence = "I just came to say hello!"
for i in range(0, len(sentence)):
	print(sentence[i])
```

```python
# Code 5
sentence = "I just came to say hello!"
for c in sentence:
	print(c)
```
