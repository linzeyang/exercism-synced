from collections import deque

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque()

    def read(self):
        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")

        return self.buffer.popleft()

    def write(self, data):
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) >= self.capacity:
            self.buffer.popleft()

        self.buffer.append(data)

    def clear(self):
        self.buffer.clear()
