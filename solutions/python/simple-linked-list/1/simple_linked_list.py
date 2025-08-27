class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self.count = 0

        for val in values:
            self.push(val)

    def __len__(self):
        return self.count

    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node
        self.count += 1

    def pop(self):
        if not self.count:
            raise EmptyListException("The list is empty.")

        node = self._head
        self._head = node.next()
        node._next = None
        self.count -= 1
        return node.value()

    def reversed(self):
        pre, head = None, self._head

        while head is not None:
            next = head._next
            head._next = pre
            pre = head
            head = next

        self._head = pre
        return self

    def __iter__(self):
        node = self._head

        while node is not None:
            yield node.value()
            node = node.next()


class EmptyListException(Exception):
    pass
