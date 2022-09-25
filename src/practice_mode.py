from random import randint
import time
import clearing

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
            actual_answer = num[0] * num[1]
            user_answer = input(f'{num[0]} * {num[1]} = ')
            if user_answer == 'q' or user_answer == 'Q':
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
            elif actual_answer == int(user_answer):
                correct_count += 1
                num = self.get_numbers()
                continue
            elif actual_answer == int(user_answer):
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