from random import randint

print('Guess THE NUMBER GAME ')
k = randint(1, 100)
points = 100
c = 0
while True:
    g = int(input('Guess anumber between 1 to 100 : '))
    try:
        if g < 0 and g > 100:
            raise ('Disaster, you dont understand english it seems')
    except ValueError:
        print('Please enter valid number')
        continue
    if g < k:
        c = c+1
        print(f'{c}  Your guess is lower than actual number try again')
    elif g > k:
        c = c+1
        print(f'{c}  Your guess is higher than actual number try again')
    else:
        print(
            f'Hurray!!! you guessed it right on {c} chance Your score is : {points-c}')
