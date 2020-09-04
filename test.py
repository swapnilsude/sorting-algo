import random
from sorting import *


l = random.sample(range(0, 100), 50)

print(bubble_sort(l))
print(selection_sort(l))
print(insertion_sort(l))
print(quick_sort(l))
print(heap_sort(l))
print(merge_sort(l))