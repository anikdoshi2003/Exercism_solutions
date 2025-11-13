def is_isogram(string):
    cleaned_string = string.lower()
    tracked_letter = set()

    for char in cleaned_string:
        if char in ("-"," "):
            continue
        if char in tracked_letter:
            return False
            break
        tracked_letter.add(char)
    return True