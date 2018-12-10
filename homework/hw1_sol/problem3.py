import math

x_1 = 0 
x_2 = 2
y_1 = 0
y_2 = 2

# option 1
output = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))

print(output)

# option 2 (mas limpio)

diff_x_sqrd = math.pow(x_1 - x_2, 2)
diff_y_sqrd = math.pow(y_1 - y_2, 2)
output = math.sqrt(diff_x_sqrd + diff_y_sqrd)

print(output)