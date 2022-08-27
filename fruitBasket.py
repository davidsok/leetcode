from operator import le
from re import L


def fruitBasket(basket):
    fruit_map = {}
    window_start = 0
    window_length = 0
    for window_end in range(len(basket)):
        right_char = basket[window_end]
        if right_char not in fruit_map:
            fruit_map[right_char] = 0
        fruit_map[right_char] += 1
        
        while len(fruit_map) > 2:
            left_char = basket[window_start]
            fruit_map[left_char] -= 1
            if fruit_map[left_char] == 0:
                del fruit_map[left_char]
            window_start += 1
        window_length = max(window_length, window_end - window_start + 1)
    return window_length

print(fruitBasket(['A', 'B', 'C', 'A', 'C']));
print(fruitBasket(['A', 'B', 'C', 'A', 'D','D']));