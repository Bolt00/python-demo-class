import random
import threading

total_wins = []
total_failed = []
total_played = []


def Math_game():
    '''This function ask users to calculate the sum of two numbers in 5 seconds.
    if answer is corrects then a score of 10 is appended to an empty list named total_score.\n
    Parameters:

    first_num (int): First number.
    second_num (int): Second number.

    returns:

    first_num + second_num
    '''
    while True:
        try:
            first_num = random.randint(1, 10)
            second_num = random.randint(1, 10)
            total_num = first_num + second_num
            print(
                'You have 5 seconds to answer or game is over. Enter "0" to end the game')
            enter = int(
                input(f'What is the sum of {first_num} + {second_num}? >>> '))
            total_played.append(1)
            input_thread = threading.Thread(target=enter, args=(5))
            input_thread.start()
            input_thread.join(timeout=5)
            if input_thread.is_alive() is False:
                if enter == total_num:
                    print(
                        f'Your answer {enter} is correct. {first_num} + {second_num} is: {enter} ✅ and a score of 10 has been added to your score board.')
                    total_wins.append(10)

                elif enter == 0:
                    print(
                        f'You have successfully abort the game and your total win is {len(total_wins)}, total failed is {len(total_failed)} with total played of {(len(total_played))} and your total score is {sum(total_wins)}')
                    break
                elif enter == None:
                    print('Your input cannot be empty.')
                else:
                    print(
                        f'Your answer {enter} is wrong. ❌ {first_num} + {second_num} is: {total_num}')
                    total_failed.append(0)
                    print(
                        f'Game over... You played {len(total_played)} times with a total win of {len(total_wins)}, a total failed of {(len(total_failed))} and a total score of {sum(total_wins)}')

                    break
            else:
                print(
                    f'Time Up! Game over! you have a total win of {len(total_wins)}, total failed of {len(total_failed)}, total played of {len(total_played)} and your total score is {sum(total_wins)}')
                break

        except:
            print('Oops! you encountered an error, your input must be numbers only.')


Math_game()
