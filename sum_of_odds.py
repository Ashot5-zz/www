""" Calculate sum of odd numbers up to the specified input """

while True:
    inp = input('Input the number: ')
    if inp.isdecimal():
        inp = int(inp)
        break

    print('[ERROR] Please enter only numbers')

count = 0
for n in range(inp + 1):
    if n % 2 == 1:
        count += n

print(count)

count = 0
for n in range(1, inp + 1, 2):
    count += n

print(count)
