import random
import string

def generate_4_random_numbers() -> list:
    return random.sample(string.digits, 4)