from random import randint
import time

# Game Mode: Different levels with increasing difficulty

def round_one():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 5)
        num2 = randint(1, 5)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 1!')
                round_two()
            else:
                continue
                
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_two():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 7)
        num2 = randint(1, 7)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 2!')
                round_three()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_three():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 3!')
                round_four()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_four():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 4!')
                round_five()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_five():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 12)
        num2 = randint(1, 12)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 5!')
                round_six()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_six():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 15)
        num2 = randint(1, 15)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 6!')
                round_six()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_seven():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 7!')
                round_eight()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_eight():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(10, 20)
        num2 = randint(10, 20)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 8!')
                round_nine()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_nine():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(10, 100)
        num2 = randint(10, 100)
        answer = int(input(f'{num1} * {num2} = '))
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 9!')
                round_ten()
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_ten():
    correct_count = 0
    incorrect_count = 0
    while correct_count < 10:
        num1 = randint(1, 12)
        num2 = randint(1, 12)
        num3 = randint(1, 12)
        answer = int(input(f'{num1} * {num2} * {num3} = '))
        if num1 * num2 * num3 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Woohoo!!!! Congratulations you have completed the entire challenge! You are a champion!')
                break
            else:
                continue
        else:
            incorrect_count +=1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue