import random
from typing import List


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    if min < 1:
        print("Min value must be greater than 1")
        return
    elif max <= min:
        print("Max value must be more than min value")
        return
    elif max >= 1000:
        print("Max value must be less than 1000")
        return
    elif quantity < min or quantity > max:
        print("Quantity must be between min and max values")
        return
    else:
        unique_values = set()
        while len(unique_values) < quantity:
            unique_values.add(random.randint(min, max))
        result = list(unique_values)
        result.sort()
        return result


# lottery_numbers = get_numbers_ticket(-1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)
# lottery_numbers = get_numbers_ticket(1, 1, 6)
# print("Ваші лотерейні числа:", lottery_numbers)
# lottery_numbers = get_numbers_ticket(1, 1000, 3)
# print("Ваші лотерейні числа:", lottery_numbers)
# lottery_numbers = get_numbers_ticket(1, 2, 3)
# print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
