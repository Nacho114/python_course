def sum_of_n(n):
    accum = 0
    for k in range(n+1):
        accum += k
    return accum

def sum_of_n_fast(n):
    return int(( n * (n + 1) ) / 2)


k = 1000000000
# print(sum_of_n(k))
print(sum_of_n_fast(k))

