def calc(a, b, op):
    result = None
    
    if op == "a" or "A":
        result = int(a) + int(b)
    elif op == "s" or "S":
        result = int(a) - int(b)
    elif op == "m" or "M":
        result = int(a) * int(b)
    elif op == "d" or "D":
        result = int(a) / int(b)
    else:
        pass
    
    return result