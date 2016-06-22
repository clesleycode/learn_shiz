
def reverse_string(item):
    string = list(item)
    for i in range(0, (len(string)/2)):
        buff = string[i]
        string[i] = string[len(string)-i-1]
        string[len(string)-i-1] = buff
    print("".join(string).lower())

reverse_string("this is a string")
