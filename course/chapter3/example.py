def int_from_cmd(prompt):
    return int(input(prompt))

def print_member(member):
    print('Name: ', member[0], ', age: ', member[1])

def print_member_list(member_list):
    iter = 0
    print('Members:')
    while iter < len(member_list):
        print_member(member_list[iter])
        iter = iter + 1

def mean(numbers):
    nb_numbers = len(numbers)
    iter = 0
    mean_value = 0
    while iter < nb_numbers:
        mean_value = mean_value + numbers[iter]
        iter = iter + 1

    return mean_value / nb_numbers




nb_people = int_from_cmd('Insert number of people: ')


iter = 0

members = []

print('-'*25)
while iter < nb_people:
    name = input('Insert member name: ')
    age = int_from_cmd('Insert memeber age: ')
    member_data = [name, age]
    members.append(member_data)
    iter = iter + 1

    print('-'*25)


print_member_list(members)

# Calculate mean of users

ages = []
iter = 0
while iter < len(members):
    next_age = members[iter][1]
    ages.append(next_age)
    iter = iter + 1

print('-'*25)

mean_age = mean(ages)
print('Mean age:', mean_age)



