from random import randint
import time

# Game Mode: Different levels with increasing difficulty

def round_one():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 20.00:
                    print(f'Well done you have completed round 1 in {duration} seconds!')
                    round_two()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_two():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 20.00:
                    print(f'Well done you have completed round 2 in {duration} seconds!')
                    round_two()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_three():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 20.00:
                    print(f'Well done you have completed round 3 in {duration} seconds!')
                    round_three()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_four():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 40.00:
                    print(f'Well done you have completed round 4 in {duration} seconds!')
                    round_five()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_five():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 40.00:
                    print(f'Well done you have completed round 5 in {duration} seconds!')
                    round_six()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_six():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 40.00:
                    print(f'Well done you have completed round 6 in {duration} seconds!')
                    round_seven()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_seven():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 60.00:
                    print(f'Well done you have completed round 7 in {duration} seconds!')
                    round_eight()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_eight():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 60.00:
                    print(f'Well done you have completed round 8 in {duration} seconds!')
                    round_nine()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')


def round_nine():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 120.00:
                    print(f'Well done you have completed round 9 in {duration} seconds!')
                    round_ten()
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

def round_ten():
    correct_count = 0
    incorrect_count = 0
    start_time = time.time()
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
                duration = round(time.time() - start_time, 2)
                if duration < 120.00:
                    print(f'Woohoo!!!! Congratulations you have completed the entire challenge! You are a champion! You completed round 1 in {duration} seconds!')
                    return
                else:
                    print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                    break
            else:
                continue
                    
        else:
            print('Incorrect answer')
            incorrect_count += 1
            if incorrect_count == 3:
                print('Sorry you are out of the game! Better luck next time!')

