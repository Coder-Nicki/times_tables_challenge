from random import randint
import time

def hello():
    print('hello')

# Practice mode
def easy_practise():
    correct_count = 0
    incorrect_count = 0
    num1 = randint(1, 7)
    num2 = randint(1, 7)
    answer = int(input(f'{num1} * {num2} = '))
    while answer != 'quit':
        if num1 * num2 == answer:
            correct_count += 1
            continue
        else:
            incorrect_count +=1
            continue
    return correct_count and incorrect_count

def medium_practise():
    correct_count = 0
    incorrect_count = 0
    num1 = randint(1, 12)
    num2 = randint(1, 12)
    answer = int(input(f'{num1} * {num2} = '))
    while answer != 'quit':
        if num1 * num2 == answer:
            correct_count += 1
            continue
        else:
            incorrect_count +=1
            continue
    return correct_count and incorrect_count

def hard_practise():
    correct_count = 0
    incorrect_count = 0
    num1 = randint(10, 10)
    num2 = randint(10, 10)
    answer = int(input(f'{num1} * {num2} = '))
    while answer != 'quit':
        if num1 * num2 == answer:
            correct_count += 1
            continue
        else:
            incorrect_count +=1
            continue
    return correct_count and incorrect_count