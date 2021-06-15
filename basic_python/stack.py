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
    left_bracket = '('
    right_bracket = ')'

    if not isinstance(s, str) or (s and s[0] == right_bracket):
        return False

    for i in s:
        if i == left_bracket:
            stack.push(i)
        else:
            if stack.isEmpty():
                return False
            stack.pop()

    return stack.isEmpty()
    
strBracket = '((()()))()'
print(parChecker(strBracket))