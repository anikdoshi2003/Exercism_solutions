def is_armstrong_number(number):
    digits = str(number)
    length_of_num = len(digits)
    
    total = 0
    for i in digits:
        total += int(i) ** length_of_num
    
    return total == number
