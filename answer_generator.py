import random
import string


class AnswerGenerator:
    @staticmethod
    def generate():
        sample_list = random.sample(string.digits, 4)
        return ''.join(sample_list)
