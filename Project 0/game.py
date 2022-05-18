import numpy as np

number = np.random.randint(1, 101)  # imagine number
count = 0

while True:
    count += 1
    imagine_number = int(input('Guess a number:'))
    if number < imagine_number:
        print('Should be less!')
    elif number > imagine_number:
        print('Should be greater!')
    else:
        print(f'You guess number in {count} try!')
        break  # end of the game
