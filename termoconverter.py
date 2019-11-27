def C2F(value: float) -> float:
    return value * 1.8 + 32


def F2C(value: float) -> float:
    return (value - 32) / 1.8


def C2K(value: float) -> float:
    return value + 273.15


def K2C(value: float) -> float:
    return value - 273.15


def F2K(value: float) -> float:
    return (value + 459.67) / 1.8


def K2F(value: float) -> float:
    return value * 1.8 - 459.67


if __name__ == '__main__':
    print('Supported temperature formats: 36.6 C | 97.88 F | 309.75 K')
    base_fmts = {'C', 'F', 'K'}

    # input the temperature
    while True:
        temp = input('Temperature: ').split()
        if len(temp) != 2:
            print('Invalid temperature format. Please insert value and format')
        elif temp[1].upper() not in base_fmts:
            print('Unsupported temperature format. Please use one of the'
                  ' followings: C(elsius) | K(elvin) | F(ahrenheit)')
        else:
            temp[0] = float(temp[0])  # this is unsafe
            temp[1] = temp[1].upper()
            break

    # input conversion format
    while True:
        new_fmt = input('Convert to (C(elsius) | K(elvin) | F(ahrenheit)): ')\
                .strip().upper()
        if new_fmt not in base_fmts:
            print('Unsupported conversion format. Please use one of the'
                  ' followings: C(elsius) | K(elvin) | F(ahrenheit)')
        else:
            break

    # perform conversion
    new_val = locals().get(
            '{}2{}'.format(temp[1], new_fmt), lambda x: x)(temp[0])

    print('Conversion result:', temp[0], temp[1].upper(),
          '= {:.3f}'.format(new_val), new_fmt.upper())
