class Heap:

    def __init__(self):
        self._heap = []
        self._current_index = None

    def add(self, value):
        self._heap.append(value)
        i = len(self._heap) - 1
        while i - 1 >= 0 and value < self._heap[(i - 1) // 2]:
            self._heap[(i - 1) // 2], self._heap[i] = (
                self._heap[i],
                self._heap[(i - 1) // 2],
            )
            i = (i - 1) // 2

    def pop(self):
        n = len(self._heap)
        if n == 1:
            return self._heap.pop()
        if n >= 2:
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            res = self._heap.pop()
            n = len(self._heap)
        i = 0
        index_left_child = 2 * i + 1
        index_right_child = 2 * i + 2
        while i < n:
            index_left_child = 2 * i + 1
            index_right_child = 2 * i + 2
            # if index_right_child <= (n - 1) and (self._heap[i] > self._heap[index_left_child] or self._heap[i] > self._heap[index_right_child]):
            #     if self._heap[index_left_child] < self._heap[index_right_child]:
            #         self._heap[i], self._heap[index_left_child] = self._heap[index_left_child], self._heap[i]
            #         i = index_left_child
            #     else:
            #         self._heap[i], self._heap[index_right_child] = self._heap[index_right_child], self._heap[i]
            #         i = index_right_child
            # elif index_left_child <= (n - 1) and self._heap[i] > self._heap[index_left_child]:
            #     self._heap[i], self._heap[i] = self._heap[index_left_child], self._heap[i]
            #     i = index_left_child
            # else:
            #     break

            # Пока не дошли до конца кучи (n - 1) и левый ребенок меньше родителя, то продолжаем спуск
            if index_left_child <= (n - 1) and self._heap[i] > self._heap[index_left_child]:
                self._heap[i], self._heap[index_left_child] = (
                    self._heap[index_left_child],
                    self._heap[i],
                )
                j = index_left_child
            if index_right_child <= (n - 1) and self._heap[i] > self._heap[index_right_child]:
                self._heap[i], self._heap[index_right_child] = (
                    self._heap[index_right_child],
                    self._heap[i],
                )
                j = index_right_child
            if i == j:
                break
            i = j
        return res

    def __str__(self):
        return str(self._heap)


heap = Heap()
heap.add(4)
heap.add(3)
heap.add(8)
heap.add(2)
heap.add(1)
heap.add(18)
print(heap)
heap.pop()
heap.pop()
heap.pop()
heap.add(2)
heap.add(25)
# heap.pop()
print(heap)
