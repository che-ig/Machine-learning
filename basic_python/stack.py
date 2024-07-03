class Stack:
    """
    Класс Stack
    """

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


def revertWord(s: str):
    revertWord = ""
    m = Stack()
    for i in s:
        m.push(i)

    while not m.isEmpty():
        revertWord += m.pop()

    return revertWord


def parChecker(s: str):
    stack = Stack()
    left_brackets = "({["
    right_brackets = ")}]"

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


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


if __name__ == "__main__":
    print(divideBy2(5))
    print(revertWord("abc"))
    strBracket = "((()()))()"
    print(parChecker("{{([][])}()}"))
    print(parChecker(strBracket))
