def translate(text):
    vowels = set("aeiou")
    starting_pattern = ("xr","yt")
    
    def translate_word(word):
        if not word:
            return word
            
        if(word[0] in vowels or word[:2] in starting_pattern):
            return word + "ay"
    
        char_store= ""
        i = 0
        
        while i < len(word):
            if word[i:i+2] == "qu":
                char_store += "qu"
                i += 2
                break
                
            if word[i] == "y" and i > 0:
                break
    
            if word[i] not in vowels:
                char_store += word[i]
                i += 1
            else:
                break
            
        return word[i:] + char_store + "ay"

    words = text.split()
    translated_words= []

    for w in words:
        translated_words.append(translate_word(w))

    return " ".join(translated_words)