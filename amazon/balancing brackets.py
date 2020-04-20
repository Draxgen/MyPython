'''
balancing brackets
'''

def balanceBrackers(brackets):
    stack = []
    for b in brackets:
        if b in ['{', '[', '(']:
            stack.append(b)
        elif b in ['}', ']', ')']:
            bracket = stack.pop()
            if bracket == '{':
                if b != '}' : return 'NO'
            elif bracket == '[':
                if b != ']' : return 'NO'
            elif bracket == '{':
                if b != '}' : return 'NO'
    return 'YES'

brackets = [r'{[()]}', r'{[(])}', r'{{[[(())]]}}']

for b in brackets:
    print(balanceBrackers(b))