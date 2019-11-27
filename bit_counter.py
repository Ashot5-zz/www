""" Calculates number of 1-s and 0-s in binary string """
​
while True:
    inp = input('Input the binary string: ')
    if set(inp).issubset({'0', '1'}):
        break
    print('[ERROR] Please enter only 0-s and 1-s')
​
counts = {'0': 0, '1': 0}
for ch in inp:
    counts[ch] += 1
​
print(counts)
