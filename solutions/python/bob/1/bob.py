def response(hey_bob):
    cleaned_str = hey_bob.strip()
    if(hey_bob.isupper() and hey_bob[-1]=="?"):
        return "Calm down, I know what I'm doing!"
    if(cleaned_str!="" and cleaned_str[-1])== "?":
        return "Sure."
    if(hey_bob.isupper()):
        return "Whoa, chill out!"
    if(cleaned_str ==" " or cleaned_str ==""):
        return "Fine. Be that way!"
    else:
        return "Whatever."