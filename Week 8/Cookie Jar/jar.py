class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ("🍪" * self._size)

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError
        self._size = size