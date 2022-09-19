from random import randint
import time

# Practice mode functions

def easy_practise():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
    while correct_count < 100:
        num1 = randint(1, 7)
        num2 = randint(1, 7)
        answer = input(f'{num1} * {num2} = ')
        if answer == 'q' or answer == 'Q':
            duration = round(time.time() - start_time, 2)
            if correct_count > 20 and incorrect_count < 3:
                print(f'You are AMAZING! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
            elif correct_count == 100:
                print(f'You are a champion! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!!')
                break
            else:
                print(f'You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
        elif num1 * num2 == int(answer):
            correct_count += 1
            continue
        else:
            incorrect_count += 1
            continue

def medium_practise():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
    while correct_count < 100:
        num1 = randint(1, 12)
        num2 = randint(1, 12)
        answer = input(f'{num1} * {num2} = ')
        if answer == 'q' or answer == 'Q':
            duration = round(time.time() - start_time, 2)
            if correct_count > 20 and incorrect_count < 3:
                print(f'You are AMAZING! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
            elif correct_count == 100:
                print(f'You are a champion! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
            else:
                print(f'You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
        elif num1 * num2 == int(answer):
            correct_count += 1
            continue
        else:
            incorrect_count += 1
            continue

def hard_practise():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
    while correct_count < 100:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        answer = input(f'{num1} * {num2} = ')
        if answer == 'q' or answer == 'Q':
            duration = round(time.time() - start_time, 2)
            if correct_count > 20 and incorrect_count < 3:
                print(f'You are AMAZING! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
            elif correct_count == 100:
                print(f'You are an absolute times table genius! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
            else:
                print(f'You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                break
        elif num1 * num2 == int(answer):
            correct_count += 1
            continue
        else:
            incorrect_count += 1
            continue
