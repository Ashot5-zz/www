""" Fill the string with specified character """

while True:
    length = input('Length: ')
    if length.isdecimal():
        length = int(length)
        break
    print('[ERROR] Please insert a number for length')

while True:
    fill = input('Fill: ')
    if len(fill) == 1:
        break
    print('[ERROR] Please insert one symbol for fill')

txt = input('Text: ')

print('{}{}'.format(fill * (length - len(txt)), txt))
