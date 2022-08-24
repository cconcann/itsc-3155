def string_both_ends(str):
    if len(str) < 2:
        return "your string is to short"
    return str[0:2] +  str[-2:]


string = input("Enter your String:")
stringToReturn = string_both_ends(string)
print(stringToReturn)


def numInc(str1, str2):
    increments = []
    num1 = str1
    num2 = str2
    x = range(num1, num2, 7)
    for n in x:    
        increments.append(n)
    return increments

x = int(input("enter first number"))
y = int(input("enter second number"))
arrayToReturn = []
arrayToReturn = numInc(x, y)
print(arrayToReturn)
