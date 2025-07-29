def binary_change(n: int):
    binary_number = bin(n)
    ordinary_number = int(binary_number, 2)

    print(f'binary_number: {binary_number}')
    print(f'ordinary_number: {ordinary_number}')

def bit_manipulate(a: int, b: int):
    a_bin = bin(a)
    b_bin = bin(b)

    print(f'a_bin: {a_bin}, b_bin: {b_bin}')

    result_and = bin(a & b)
    result_or = bin(a | b)
    result_xor = bin(a ^ b)

    print(f'AND: {result_and}')
    print(f'OR: {result_or}')
    print(f'XOR: {result_xor}')


number = 11
binary_change(number)

a = 12
b = 20
bit_manipulate(a,b)