import math

def diff_sqr(a, b):
    return math.pow(a - b, 2)

def dist(a, b, c, d):
    x_diff_2 = diff_sqr(a, b)
    y_diff_2 = diff_sqr(c, d)
    z = math.sqrt(x_diff_2 + y_diff_2)

    return z


r = 0
f = 2
s = 0
d = 3

z = dist(r, f, s, d)
print(z)


img = load('file/img')
bbox = network.pedict(img)
