

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
    right_bound = 100
    
    while True:
        trial_number = (left_bound + right_bound) // 2
        trial_count += 1
        if trial_number == number:
            return trial_count
        elif trial_number < number:
            right_bound = trial_number
        elif trial_number > number:
            left_bound = trial_number

