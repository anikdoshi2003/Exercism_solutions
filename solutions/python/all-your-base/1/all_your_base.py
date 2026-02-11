def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    output = []
    value = 0
    for digit in digits:
        value = value * input_base + digit

    if value == 0:
         return [0]
    else:
        while value > 0:
         remainder = value % output_base
         output.append(remainder)
         value = value // output_base
    output.reverse()
    
    return output
    