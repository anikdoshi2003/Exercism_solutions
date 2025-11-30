def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if(number < 1):
        raise ValueError("Classification is only possible for positive integers.")
    divisors = []
    result = 0
    for i in range(1,number-1):
        if number % i == 0:
            divisors.append(i)

    for i in divisors:
        result += i
    
    if result == number:
        return "perfect"
    elif result > number:
        return "abundant"
    else:
        return "deficient"

