import numpy as np

number = np.random.randint(1, 101)  # imagine number
count = 0

while True:
    count += 1
    imagine_number = int(input('Угадай число:'))
    if number < imagine_number:
        print('Число меньше!')
    elif number > imagine_number:
        print('Число больше!')
    else:
        print(f'Вы угадали число за {count} попыток!')
        break  # end of the game
