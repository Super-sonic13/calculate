def znak(input_operrator, znak_array):
    split_list = znak_array.split(' ')
    for i in range(len(split_list)):
        if int(input_operrator.find(split_list[i])) > -1:
            n = str(split_list[i])
    return n
def cifri(input_operrator, znak_array):
    n = znak(input_operrator, znak_array)
    cifri_list = input_operrator.split(n)
    return cifri_list
def calculate(input_operrator):
    znak_array = ('+ - / * ** %')
    cifri_list = cifri(input_operrator, znak_array)
    a = int(cifri_list[0])
    operator = znak(input_operrator, znak_array)
    b = int(cifri_list[1])
    if operator == '+':
        print('{} + {} = '.format(a, b))
        print(a + b)
    elif operator == '-':
        print('{} - {} = '.format(a, b))
        print(a - b)
    elif operator == '*':
        print('{} * {} = '.format(a, b))
        print(a * b)
    elif operator == '/':
        if b == 0:
            print('You cannot division on 0')
        else:
            print('{} / {} = '.format(a, b))
            print(a / b)
    elif operator == '%':
        print('{} % {} = '.format(a, b))
        print(a % b)
    elif operator == '**':
        print('{} ** {} = '.format(a, b))
        print(a ** b)
    else:
        print('You have not typed a valid operator, please run the program again.')

input_operrator = input('Enter the expression you want to count:\n')
print(calculate(input_operrator))
