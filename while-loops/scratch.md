# Problem Set: While Loops

## Directions

Complete all questions below.

## Practice

```python
def get_guest_count():
    done = False
    number_of_guests = 0

    while not done:
        name = input('Enter a guest name, or done to quit: ')
        if name == 'done':
            done = True
        else:
            number_of_guests += 1

    return number_of_guests

guests = get_guest_count()
print(f'There will be {guests} guest(s).')
```

```python
def get_guest_count_2():
    prompting = True
    number_of_guests = 0

    while prompting:
        name = input('Enter a guest name, or done to quit: ')
        if name == 'done':
            prompting = False
        else:
            number_of_guests += 1

    return number_of_guests

guests = get_guest_count()
print(f'There will be {guests} guest(s).')
```

```python
def get_guest_count_3():
    number_of_guests = 0

    while True:
        name = input('Enter a guest name, or done to quit: ')
        if name == 'done':
            break
        else:
            number_of_guests += 1

    return number_of_guests

guests = get_guest_count()
print(f'There will be {guests} guest(s).')
```

loop, exit if done, ignore skip, otherwise print

```python
while True:
    user_input = input('enter input: ')
    if user_input == 'done':
        break
    elif user_input == 'skip':
        continue
    print(f'you entered {user_input}')
```

equivalent for loop for while

```python
x = 5
while x > 0:
    print(x)
    x -= 1

for x in range(5):
    print(x)

for x in range(5, 0):
    print(x)

for x in range(0, 5):
    print(x)

for x in range(5, 0, -1):
    print(x)
```

equivalent for loop for while

```python
x = 0
while x < 5
    print(x)
    x += 1

for x in range(5):
    print(x)

for x in range(5, 0):
    print(x)

for x in range(0, 5):
    print(x)

for x in range(5, 0, -1):
    print(x)
```

explanation of why 

what's wrong with the following code
```python
loop_count = int(input('How many numbers should we sum? '))
x = 0
sum = 0
while x < loop_count:
   num = int(input('Enter an integer: ')) 
   sum += num
print(f'The sum of the numbers is {sum}')
```

multiple conditions in a while

implement "blackjack" (but with random number)
prompt_y_n
prompt_value

flag and step counter or multiple counters