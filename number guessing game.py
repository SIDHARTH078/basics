import random
secret=random.randint(1,20)
attempts=0
while True:
    try:
        guess=int(input('enter ur guess'))
        attempts+=1
        if guess<secret:
            print('too low')
        elif guess>secret:
            print('too high')
        else:
            print(f'yay u guessd the crct no the no was {secret} u got it in {attempts}th try')
            break
    except ValueError:
        print('enter a valid no')

