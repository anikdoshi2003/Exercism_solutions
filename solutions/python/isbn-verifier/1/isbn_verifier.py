def is_valid(isbn):
    # X = 10
    cleaned_isbn = ""
    numeric_isbn = list()
    weight = 11
    result = 0
    for digit in isbn:
        if digit != "-":
            cleaned_isbn += digit
            
    if len(cleaned_isbn) != 10:
        return False
    
    for d in cleaned_isbn[:-1]:
        if not d.isdigit():
            return False
    
    if cleaned_isbn[9] != "X" and not cleaned_isbn[9].isdigit():
        return False
    
    for i in cleaned_isbn[:-1]:
        if i.isdigit():
            numeric_isbn.append(int(i))
            
    if cleaned_isbn[9] == "X":
        numeric_isbn.append(10)
    else:
        numeric_isbn.append(int(cleaned_isbn[9]))
    
    for i in numeric_isbn:
        result += i * (weight-1)
        weight = weight -1
    
    if (result) % 11 == 0:
        return True
    else:
        return False
