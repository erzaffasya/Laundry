from typing import List, Any


class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def rear(self):
        return self.items[0]

    def front(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def open(self):
        return self.items

    def getdata(self, i, j):
        return self.items[i][j]