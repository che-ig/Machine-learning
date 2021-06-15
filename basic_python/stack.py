class Stack:
    '''
        Класс Stack
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return False if len(self.items) else True
    
    def push(self, object):
        self.items.append(object)

    def pop(self):
        return self.items.pop()
    
    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

m = Stack()

s = 'abc'
revertWord = ''
for i in s:
    m.push(i)

while not m.isEmpty():
    revertWord += m.pop()

print(revertWord)


def parChecker(s: str):
    stack = Stack()
    left_brackets = '({['
    right_brackets = ')}]'

    def matches(open, close):       
        return left_brackets.index(open) == right_brackets.index(close)

    if not isinstance(s, str) or (s and s[0] in right_brackets):
        return False

    for i in s:
        if i in left_brackets:
            stack.push(i)
        else:
            if stack.isEmpty():
                return False
            else:
                top = stack.pop()
                if not matches(top, i):
                    return False

    return stack.isEmpty()




strBracket = '((()()))()'
print(parChecker('{{([][])}()}'))
print(parChecker(strBracket))