import random

#Dice roll simulation

def dice_roll(times):
    for time in range(times):
        print(f'Time {time+1}:')
        print(f'The dice roll: {random.randint(1,6)}')

#Random Numbers in list
def random_list():
    rand_num=[]
    for num in range(5):
        rand_num.append(random.randint(1,100))
    print('Random Numbers in the list: ',rand_num)

#Guess the number game
def Guess_num():
    num=random.randint(1,50)
    i=1
    while i<=30:
        print(f'\nAttempt {i}:')
        guessed=int(input('Guess an integer between 1 and 50: '))
        if guessed==num:
            print(f"{f'\nThe guessed number {guessed} in correct!!':=>67}")
            print('='*33)
            break
        else:
            print('\nTry again!!')
            i+=1
    else:
        print(f'the correct number was {num}')       
