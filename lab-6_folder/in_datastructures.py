def bark(prompt):
    return f'woof! {prompt}'
functions = [bark, str.lower, str.capitalize]
print(functions[0]('Roshani Sisimanu'))
print(functions[1]('ABCD'))
print(functions[2]('dasjkfh asjkfha'))
