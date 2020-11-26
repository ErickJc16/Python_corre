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

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(range(len(cars_minute)),cars_minute,c='red')
plt.plot(range(len(moving_average)),moving_average,c='blue')

plt.title("Moving Average Filter", fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Cars", fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
