import random

random_number = [random.randint(1, 100) for i in range(20)]
par_number = list(filter(lambda x: x % 2 == 0, random_number))
print(random_number)
print(par_number)
