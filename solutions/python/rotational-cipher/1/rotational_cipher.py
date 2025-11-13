def rotate(text, key):
    result = ""
    for char in text:
        if char.islower():
            index = ord(char) - ord('a')
            rotated = (index + key) % 26
            new_char = chr(rotated + ord('a'))
            result += new_char
        elif char.isupper():
            index = ord(char) - ord('A')
            rotated = (index + key) % 26
            new_char = chr(rotated + ord('A'))
            result += new_char
        else:
            result += char
    return result