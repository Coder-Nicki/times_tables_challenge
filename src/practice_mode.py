from random import randint
import time
import clearing

class RangeError(Exception):
    pass

# Practice mode functions

class Practice:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def practise_mode(self):
        correct_count = 0
        incorrect_count = 0
        start_time = time.time()
        while correct_count < 100:
            num = self.get_numbers()
            answer = input(f'{num[0]} * {num[1]} = ')
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
            elif num[0] * num[1] == int(answer):
                correct_count += 1
                num = self.get_numbers()
                continue
            else:
                incorrect_count += 1
                num = self.get_numbers()
                continue

    def get_numbers(self):
        num1 = randint(self.x, self.y)
        num2 = randint(self.x, self.y)
        return num1, num2 

def practice_number():
        correct = 0
        incorrect = 0
        number = int(input('What number would you like to practise multiplying by between 1 and 12: '))
        if not number in range(1, 13):
            raise RangeError(f'You entered {number}. You must enter a number between 1 and 12')
        while correct < 50:
            number_two = randint(1, 12)
            try:
                user_answer = input(f'{number} * {number_two} = ')
            except RangeError:
                print('Not in range')
            if number * number_two == user_answer:
                count += 1
            elif user_answer == 'q':
                print(f'You got {correct} correct and made {incorrect} errors!')
                time.sleep(3)
                clearing.clear()
                return
            else:
                incorrect += 1



