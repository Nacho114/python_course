
# shopping_list = ['carrots', 'milk', 'trycicle',
#                  'retarded clown', 'papel', 'beer']


# for k in range(100):
#     print(k)

# max_val = 10
# prompt = 'Insert number larger than ' + str(max_val) + ': '
# nber = int(input(prompt))

# while nber <= 10:
#     nber = int(input(prompt))

def ask_password():
    return input('insert password: ')

def message(in_pass, true_pass):
    if in_pass != true_pass:
        print('Incorrect password, please try again!')
    else:
        print('Success, logged in!')

true_pass = 'password'

in_pass = ask_password()
message(in_pass, true_pass)

while in_pass != true_pass:
    in_pass = ask_password()
    message(in_pass, true_pass)





