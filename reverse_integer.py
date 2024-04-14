number = -876
strNum = str(number)
if number > 0:
    print(strNum[::-1])
else:
    num = strNum[:0:-1] * -1
    print(num)
