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
