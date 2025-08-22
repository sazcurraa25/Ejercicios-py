def comparison(number1, number2):
    if number1<number2:
        return "-1"
    elif number1>number2:
        return "1"
    else:
        return "0"
compare = comparison(input("Dame un número: "), input("Dame un número: ")) 
print(compare)