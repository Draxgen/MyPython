input = 'this is a string'
print('Original String:', input)
output = ''

## Reverse the string
stack = []
for x in input:
    stack.append(x)

for x in range(len(stack)):
    output += stack.pop()

print('Reverse string:',output)

## To upper case
print('To upper case:', input.upper())


