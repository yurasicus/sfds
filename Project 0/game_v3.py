import numpy as np

def score_game(predict_func) -> float:
    """ Makes 1000 runs of given input function.
        Returns average attempts count made until win.
        
    Args:
        predict_func (_type_): tested function

    Returns:
        float: average attempts count until win
    """
    
    total_runs = 1000                   # number of runs
    total_trials = 0
    
    for _ in range(total_runs):
        test_number = np.random.randint(1, 101)
        # print(f'trying {test_number} number, run {_}')
        total_trials += predict_func(test_number)  # total attempt count in run
    
    # average attempt count in 1000 runs:
    return total_trials / total_runs  


def smart_predict(number:int=1) -> int:
    """ Function predict a proposed number.
        It takes into account if a number is less or greater
        than given.

    Args:
        number (int, optional): number to guess. Defaults to 1.

    Returns:
        int: Number of attempts until guess
    """    
    
    trial_count = 0
    left_bound = 0
    right_bound = 100 + 1
    
    while True:
        trial_number = (left_bound + right_bound) // 2
        # print(left_bound, trial_number, right_bound)
        trial_count += 1
        if trial_number == number:
            return trial_count
        elif trial_number > number:
            right_bound = trial_number
        elif trial_number < number:
            left_bound = trial_number


if __name__ == '__main__':
    print(score_game(smart_predict))
