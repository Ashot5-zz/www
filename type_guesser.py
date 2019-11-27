""" Guess the type of the input """

# get the input and remove minus sign from the left
inp = input('Hit me: ').lstrip('-')
msg = 'You hitted me with "{}"'

if inp.isdecimal():
    print(msg.format('int'))
elif inp[0] != '.' and inp[-1] != '.' and inp.replace('.', '', 1).isdecimal():
    print(msg.format('float'))
else:
    print(msg.format('str'))
