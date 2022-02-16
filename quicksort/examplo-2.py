from cmath import pi
import random

def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) < 2:
        return array
    else:
        pivo = random.choice(array)
        
        for x in array:
            if x < pivo:
                less.append(x)
            elif x == pivo:
                equal.append(x)
            else:
                greater.append(x)

        return quicksort(less) + equal + quicksort(greater)

print(quicksort([5, 3, 6, 2, 10, 1, 4, 7, 8, 9]))

# Prefira sempre pegar um valor qualquer para o pivo