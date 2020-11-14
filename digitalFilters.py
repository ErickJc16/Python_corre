#Pag 171 "Understanding Digital Signal Processing"
from matplotlib import pyplot as plt 

cars_minute = [10,22,24,42,37,77,89,22,63,9]

window_size = 5

i = 0

moving_average = []

while i < len(cars_minute) - window_size + 1:
    new_window = cars_minute[i: i + window_size]

    window_average = sum(new_window) / window_size
    moving_average.append(window_average)

    i += 1

print(moving_average)



