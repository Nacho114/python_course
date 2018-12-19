def mean(numbers):
    nb_numbers = len(numbers)
    iter = 0
    mean_value = 0
    while iter < nb_numbers:
        mean_value = mean_value + numbers[iter]
        iter = iter + 1

    return mean_value / nb_numbers




k = [1, 2, 3, 4]

print(mean(k))