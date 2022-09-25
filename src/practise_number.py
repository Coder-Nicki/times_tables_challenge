from random import randint
import clearing
import time

class RangeError(Exception):
    pass

def get_int():
    number = int(input('What number would you like to practise multiplying by between 1 and 12: '))
    if not number in range(1, 13):
        raise RangeError(f'You entered {number}. You must enter a number between 1 and 12')
    return number

def practice_number():
        correct_answer = 0
        incorrect = 0
        while True:
            try:
                user_number = get_int()
                break
            except RangeError as err:
                print(err.args)
            except ValueError:
                print('You must enter a number between 1 and 12')
        # while correct_answer < 50:
        for i in range(20):
                    number_two = randint(1, 12)
                    user_answer = input(f'{user_number} * {number_two} = ')
                    answer = user_number * number_two
                    if user_answer == 'q':
                        print(f'You got {correct_answer} correct and made {incorrect} error/s!')
                        time.sleep(3)
                        clearing.clear()
                        return
                    elif answer == int(user_answer):
                        correct_answer += 1
                    else:
                        incorrect += 1
        print(f'You got {correct_answer} correct and made {incorrect} error/s!')
        time.sleep(3)
        clearing.clear()
