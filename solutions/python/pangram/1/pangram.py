def is_pangram(sentence):
    cleaned_sentence = sentence.lower().strip()
    seen_letters = set()
    for char in cleaned_sentence:
        if char.isalpha():
            if char not in seen_letters:
                seen_letters.add(char)
        else:
            continue
        
    if len(seen_letters) == 26:
        return True
    else:
        return False