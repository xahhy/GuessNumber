from answer_generator import AnswerGenerator
from compare_number import CompareNumber


class Guess:
    INPUT_LENGTH_ERROR = 'Input length invalid. Please input 4 numbers!'
    INPUT_NOT_NUMBERS = 'Cannot input none-numeric!'
    INPUT_HAS_DUPLICATE_NUMBERS = 'Cannot input duplicate numbers!'
    INPUT_LEGAL = 'Success'

    def __init__(self):
        self.answer = AnswerGenerator.generate()

    def guess(self, input_string):
        is_legal, message = self.is_input_legal(input_string)
        if is_legal:
            return CompareNumber.compare(self.answer, input_string)
        else:
            return message

    def is_input_legal(self, input_string: str):
        try:
            if (len(input_string) != 4):
                raise Exception(self.INPUT_LENGTH_ERROR)
            if (not input_string.isdigit()):
                raise Exception(self.INPUT_NOT_NUMBERS)
            if (len(input_string) != len(set(input_string))):
                raise Exception(self.INPUT_HAS_DUPLICATE_NUMBERS)
        except Exception as e:
            return False, str(e)
        else:
            return True, self.INPUT_LEGAL
