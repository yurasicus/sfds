import numpy as np

def random_predict(number:int=1) -> int:
    """ this function randomly guesses a number

    Args:
        number (int, optional): Given proposed number. Defaults to 1.

    Returns:
        int: number of tries until win
    """

    count = 0
    
    while True:
        predict_number = np.random.randint(1, 101)
        count += 1
        if number == predict_number:
            return count


def score_game(predict_func) -> float:
    """ Makes 1000 runs of given input function.
        Returns average try count made until win.
        
    Args:
        predict_func (_type_): tested function

    Returns:
        float: average try count until win
    """
    
    total_runs = 1000                   # number of runs
    total_trials = 0
    
    for _ in range(total_runs):
        total_trials += predict_func()  # total try count in run
    
    return total_trials / total_runs  # average try count in 1000 runs


# print(f'Average try count to win: {random_predict()}')

if __name__ == '__main__':
    print(score_game(random_predict))
