def indices(text : str) :
    return list(i for i in range(len(text)) if 65 <= ord(text[i]) <= 90)

print(indices("PYthOn"), indices("6pYthOn1"))
