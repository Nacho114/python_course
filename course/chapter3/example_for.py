def int_from_cmd(prompt):
    return int(input(prompt))

def print_member(member):
    print('Name: ', member[0], ', age: ', member[1])

def print_member_list(member_list):
    print('Members:')
    for member in member_list:
        print_member(member)
    
def mean(numbers):
    mean_value = 0
    for nber in numbers:
        mean_value += nber

    return mean_value / len(numbers)


nb_people = int_from_cmd('Insert number of people: ')

members = []
print('-'*25)
for _ in range(nb_people):
    name = input('Insert member name: ')
    age = int_from_cmd('Insert memeber age: ')
    member_data = [name, age]
    members.append(member_data)

    print('-'*25)


print_member_list(members)

# Calculate mean of users
ages = []
for mber in members:
    ages.append(mber[1])

print('-'*25)

mean_age = mean(ages)
print('Mean age:', mean_age)
