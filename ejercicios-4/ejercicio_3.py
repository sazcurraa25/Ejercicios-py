# import random

# random_number = [random.randint(1, 100) for i in range(5)]

# getNumbers =  lambda a:map( a * a, random_number)

# print(getNumbers)

random_number = int(input("ingresa un número: "))

def elevatenumbers(getNumbers):
    return (getNumbers*getNumbers)

gotNumbers = elevatenumbers(random_number)

print(gotNumbers)

