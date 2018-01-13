import random
import string

INPUT_NOT_NUMBERS = '输入不是纯数字'
INPUT_LENGTH_ERROR = '输入字符个数不是4'

INPUT_LEGAL = '输入合法'


def generate_4_random_numbers() -> list:
    return random.sample(string.digits, 4)


def is_input_legal(input_string: string):
    try:
        if (len(input_string) != 4):
            raise Exception(INPUT_LENGTH_ERROR)
        if (not input_string.isdigit()):
            raise Exception(INPUT_NOT_NUMBERS)
    except Exception as e:
        return False, str(e)
    else:
        return True, INPUT_LEGAL


def calculate_result(input_string, expect_string):
    A, B = 0, 0
    for index, number in enumerate(input_string):
        if number == expect_string[index]:
            A += 1
        elif number in expect_string:
            B += 1
    return A, B


if __name__ == '__main__':
    expect_number = ''.join(generate_4_random_numbers())
    while True:
        input_string = input('请输入4位数字:')
        legal, message = is_input_legal(input_string)
        if legal:
            A, B = calculate_result(input_string, expect_number)
            print(A, 'A', B, 'B')
            if (A, B) == (4, 0):
                print('猜对了！')
                break
        else:
            print('输入不合法，因为', message)
