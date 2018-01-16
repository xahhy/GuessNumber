from guess import Guess

def generate_input_message(remain_times:int):
    return 'Please input your number(%s):'%remain_times


if __name__ == '__main__':
    print('Welcome!')
    remain_times = 6
    guess = Guess()
    while remain_times is not 0:
        input_string = input(generate_input_message(remain_times))
        result = guess.guess(input_string)
        if result == '4A0B':
            print('Congratulations!')
            break
        else:
            remain_times -= 1
            print(result)
    if remain_times is 0:
        print('Game Over')