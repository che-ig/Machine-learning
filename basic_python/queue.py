class Queue:
    __size__ = 0
    __top__ = None
    __next__ = None
    __prev__ = None

    def __init__(self):
        pass

    def enqueue(self, value):
        obj = {
            'value': value,
            'next': None,
            'prev': self.__prev__
        }
        if self.isEmpty():
            self.__top__ = obj
        self.__size__ += 1
        if self.__prev__:
            self.__prev__['next'] = obj

        self.__prev__ = obj

    def dequeue(self):
        if not self.isEmpty():
            top  = self.__top__
            self.__top__ = self.__top__['next']
            
            return top

    def getSize(self):
        return self.__size__
    
    def isEmpty(self):
        return self.__size__ < 1
q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    for item in range(q.getSize()):
        top = q.dequeue()
        print(top.get('value'))
        