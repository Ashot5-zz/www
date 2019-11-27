def cast_operand(opr: str):
    if opr.isdecimal():
        return int(opr)
    if opr.replace('.', '', 1).isdecimal():
        return float(opr)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return None
    return a / b


print('This calculator takes expressions in polish'
      ' notation so please follow the rules')

OPERATIONS = {
    '+': 'add',
    'add': 'add',
    '-': 'sub',
    'sub': 'sub',
    '*': 'mul',
    'mul': 'mul',
    '/': 'div',
    'div': 'div'
}

while True:
    expr = input('Expression: ').split()

    if len(expr) != 3:
        print('[ERROR] Invalid expression format')
        continue

    if expr[0] not in OPERATIONS:
        print('[ERROR] Invalid operation')
        continue

    valid = True
    for idx in range(1, 3):
        expr[idx] = cast_operand(expr[idx])
        if expr[idx] is None:
            valid = False
            print('[ERROR] Invalid type for operand', idx)
            break

    if valid:
        break

print(f"{expr[0]} {expr[1]} {expr[2]} =",
      globals()[OPERATIONS[expr[0]]](expr[1], expr[2]))
