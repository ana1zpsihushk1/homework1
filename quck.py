import random

def quicksort_simple_dimple_popit_squish(arr):
    if len(arr) <= 1:
        return arr
    pivo = random.choice(arr)
    left = [x for x in arr if x < pivo]
    middle = [x for x in arr if x == pivo]
    right = [x for x in arr if x > pivo]
    return quicksort_simple_dimple_popit_squish(left) + middle + quicksort_simple_dimple_popit_squish(right)

print(quicksort_simple_dimple_popit_squish([3, 6, 8, 10, 1, 2, 1]))
