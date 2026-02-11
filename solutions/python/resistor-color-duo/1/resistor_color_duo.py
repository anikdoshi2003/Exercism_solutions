
def value(colors):
    colors_dict = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }
    result = ""
    input = colors[:2]
    for color in input:
        result += colors_dict[color]
        
    return int(result)