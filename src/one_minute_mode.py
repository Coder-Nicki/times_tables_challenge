import time
from random import randint
import clearing

delay = 60 * 1
close_time = time.time()+delay
        
def one_minute_race():
    correct_count = 0
    incorrect_count = 0
    time.sleep(2)
    get_ready()
    while True:
        num1 = randint(1, 12)
        num2 = randint(1, 12)

        while True:
            try: 
                answer = int(input(f'{num1} * {num2} = '))
                clearing.clear
            except ValueError:
                print('Input must be an integer')
            else:
                break
        if num1 * num2 == answer:
            correct_count += 1         
        else:
            incorrect_count += 1
            print('Wrong')

        if time.time()>close_time:
            print(f'\nTime\'s Up!\n')
            time.sleep(2)
            print(f'You got {correct_count} correct and you made {incorrect_count} error/s')
            time.sleep(2)
            break

def get_ready():
    print('You have 1 minute to answer as many questions as you can!\n')
    time.sleep(2)
    print('Are you ready?\n')
    time.sleep(1)
    print('Get Set!\n')
    time.sleep(1)
    print('Go!\n')
    time.sleep(1)
    clearing.clear()



        
    

