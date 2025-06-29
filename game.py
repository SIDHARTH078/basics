import random
secret=random.randint(1,20)
attemts=0
while True:
    n=int(input('enter no to guess'))
    attemts+=1
    if n==secret:
        print("youre right")
        break
    else:
        print("try again")
