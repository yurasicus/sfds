import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно пытаемся угадать число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: количество попыток за которое угадал
    """

    count = 0
    
    while True:
        predict_number = np.random.randint(1, 101)
        count += 1
        if number == predict_number:
            return count


def score_game(predict_func) -> float:
    """ За какое количество попыток в среднем тестируемая функция
        угадывает число (1000 прогонов)

    Args:
        predict_func (_type_): тестируемая функция

    Returns:
        float: среднее количество попыток
    """
    
    total_runs = 1000                   # количество прогонов
    total_trials = 0
    
    for _ in range(total_runs):
        total_trials += predict_func()  # общее количество попыток
    
    return total_trials / total_runs  # среднее количество попыток при 1000 прогонов


# print(f'Количество попыток: {random_predict()}')

if __name__ == '__main__':
    print(score_game(random_predict))
