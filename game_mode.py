from random import randint
import time

# Game Mode: Different levels with increasing difficulty

def round_one():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(1, 5)
        num2 = randint(1, 5)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
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

def round_two():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(1, 7)
        num2 = randint(1, 7)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 2!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_three():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 3!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue
def round_four():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(1, 12)
        num2 = randint(1, 12)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
                return
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 4!')
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_five():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(1, 15)
        num2 = randint(1, 10)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 5!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_six():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(15, 15)
        num2 = randint(15, 15)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 6!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_seven():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(20, 20)
        num2 = randint(20, 20)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 7!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_eight():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(50, 50)
        num2 = randint(50, 50)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 8!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_nine():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(100, 100)
        num2 = randint(100, 100)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Well done you have completed round 9!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue

def round_ten():
    correct_count = 0
    incorrect_count = 0
    while incorrect_count < 3:
        num1 = randint(12, 12)
        num2 = randint(12, 12)
        num3 = randint(12, 12)
        while True:
            try: 
                answer = int(input(f'{num1} * {num2} * {num3} = '))
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 * num3 == answer:
            correct_count += 1
            if correct_count == 10:
                print('Woohoo!!!! Congratulations you have completed the entire challenge! You are a champion!')
                return
            else:
                continue
                    
        else:
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')
                continue
