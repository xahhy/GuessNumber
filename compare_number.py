class CompareNumber:
    @staticmethod
    def compare(answer_string, input_string):
        A, B = 0, 0
        for index, number in enumerate(input_string):
            if number == answer_string[index]:
                A += 1
            elif number in answer_string:
                B += 1
        return '%sA%sB' % (A, B)
