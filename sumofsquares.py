num_1 = int(input('Enter number 1 : '))
num_2 = int(input('Enter number 2 : '))
if num_1 % 2 != 0 and num_2 % 2 != 0:
    print(f'Sum of squares of {num_1} and {num_2} is : {num_1 ** 2} + {num_2 ** 2} = {(num_1 ** 2) + (num_2 ** 2)}')
else:
     print('Calculation not performed, numbers are even')