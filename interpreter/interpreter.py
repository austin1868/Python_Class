expression = input("Enter an arithmetic expression in the format 'x y z': ")

x, y, z = expression.split()

x= int(x)
z= int(z)

match y:
    case '+':
        out = x + z
    case '-':
        out = x - z
    case '*':
        out = x * z
    case '/':
        out = x / z
    case _:
        out = ('Invalid operator!')
        exit()

print(f'{out:.1f}')