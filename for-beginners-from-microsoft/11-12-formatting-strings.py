first_name = input('enter your first name: ')
last_name = input('enter your last name: ')

print('hello, {} {}'.format(first_name.capitalize(), last_name.capitalize()))
print('hello, {0} {1}'.format(first_name.capitalize(), last_name.capitalize()))
print('hello, {} {}'.format(first_name.capitalize(), last_name.capitalize()))

output = 'Hello, ' + first_name + ' ' + last_name
print(output)
output = 'Hello, {} {}'.format(first_name, last_name)
print(output)
output = 'Hello, {1} {0}'.format(first_name, last_name)
print(output)
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)
