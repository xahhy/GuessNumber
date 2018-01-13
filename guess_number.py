import random
import string

INPUT_LENGTH_ERROR = '输入字符个数不是4'


def generate_4_random_numbers() -> list:
    return random.sample(string.digits, 4)


def is_input_legal(input_string):
    try:
        if(len(input_string) != 4):
            raise Exception(INPUT_LENGTH_ERROR)

    except Exception as e:
        return False, str(e)
    else:
        return True