from Stack import Stack

parenthesesSequenceString = input()
parenthesesSequence = Stack()
pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}
balanced = True

for element in parenthesesSequenceString:
    if element in '{[(':
        parenthesesSequence.push(element)
    else:
        if parenthesesSequence.count() > 0:
            lastOpeningBracket = parenthesesSequence.pop()
            if pairs[lastOpeningBracket] != element:
                balanced = False
                break
        else:
            balanced = False

if balanced:
    print('YES')
else:
    print('NO')
