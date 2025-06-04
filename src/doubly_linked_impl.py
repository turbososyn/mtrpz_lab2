Character = str
class InvalidIndexError(Exception): pass
class CharacterTypeError(Exception): pass
def is_character(element) -> bool:
    return isinstance(element, str) and len(element) == 1

class Node:
    def __init__(self, data: Character = None, next_node: 'Node' = None, prev_node: 'Node' = None):
        if data is not None and not is_character(data):
            raise CharacterTypeError(f"Node data must be a single character string or None. Got: {data}")
        self.data: Character = data
        self.next: Node | None = next_node
        self.prev: Node | None = prev_node

    def __repr__(self):
        return f"Node(data={self.data!r})"

class DoublyLinkedList:
    def __init__(self, initial_data=None):
        self._head: Node | None = None
        self._tail: Node | None = None
        self._length: int = 0
        if initial_data:
             for item in initial_data:
                  self.append(item)

    def __str__(self) -> str:
        items = []
        current = self._head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"[{', '.join(items)}]"

    def __repr__(self) -> str:
        return f"DoublyLinkedList(length={self._length})"

    def length(self) -> int:
        return self._length

    def append(self, element: Character) -> None:
        if not is_character(element):
            raise CharacterTypeError(f"Can only append a single character string. Got: {element}")
        new_node = Node(element)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._length += 1

    def _get_node_at_index(self, index: int) -> Node:
         if not (0 <= index < self._length):
              raise InvalidIndexError(f"Internal Error: Node index {index} out of bounds (0 to {self._length - 1})")
         if index < self._length // 2:
             current = self._head
             for _ in range(index):
                 current = current.next
             return current
         else:
             current = self._tail
             for _ in range(self._length - 1, index, -1):
                 current = current.prev
             return current

    def insert(self, element: Character, index: int) -> None:
        if not is_character(element):
            raise CharacterTypeError(f"Can only insert a single character string. Got: {element}")
        if not (0 <= index <= self._length):
             raise InvalidIndexError(f"Index {index} is out of bounds for insertion (0 to {self._length})")
        if index == self._length:
            self.append(element)
        elif index == 0:
            new_node = Node(element, next_node=self._head)
            if self._head:
                self._head.prev = new_node
            self._head = new_node
            if not self._tail:
                self._tail = new_node
            self._length += 1
        else:
            existing_node = self._get_node_at_index(index)
            prev_node = existing_node.prev
            new_node = Node(element, next_node=existing_node, prev_node=prev_node)
            prev_node.next = new_node
            existing_node.prev = new_node
            self._length += 1

    def delete(self, index: int) -> Character:
        if not (0 <= index < self.length()):
            raise InvalidIndexError(f"Index {index} is out of bounds for deletion (0 to {self.length() - 1})")
        node_to_delete = self._get_node_at_index(index)
        data = node_to_delete.data
        prev_node = node_to_delete.prev
        next_node = node_to_delete.next
        if prev_node:
            prev_node.next = next_node
        else:
            self._head = next_node
        if next_node:
            next_node.prev = prev_node
        else:
            self._tail = prev_node
        node_to_delete.next = None
        node_to_delete.prev = None
        node_to_delete.data = None
        self._length -= 1
        if self._length == 0:
             self._head = None
             self._tail = None
        return data

    def deleteAll(self, element: Character) -> None:
        if not is_character(element):
             return
        current = self._head
        while current:
            next_item = current.next
            if current.data == element:
                prev_node = current.prev
                next_node = current.next
                if prev_node:
                    prev_node.next = next_node
                else:
                    self._head = next_node
                if next_node:
                    next_node.prev = prev_node
                else:
                    self._tail = prev_node
                self._length -= 1
                current.next = None
                current.prev = None
                current.data = None
            current = next_item
        if self._length == 0:
             self._head = None
             self._tail = None

    def get(self, index: int) -> Character:
        node = self._get_node_at_index(index)
        return node.data

    def clone(self) -> 'DoublyLinkedList':
        new_list = DoublyLinkedList()
        current = self._head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        if self._length <= 1:
            return
        current = self._head
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            current = next_node
        self._head, self._tail = self._tail, self._head

    def findFirst(self, element: Character) -> int:
        if not is_character(element):
             return -1
        current = self._head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: Character) -> int:
        if not is_character(element):
             return -1
        current = self._tail
        index = self._length - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    def extend(self, elements: 'DoublyLinkedList') -> None:
        if not isinstance(elements, DoublyLinkedList):
             raise TypeError("Can only extend with another DoublyLinkedList instance.")
        if elements.length() == 0:
             return
        if self.length() == 0:
             self._head = None
             self._tail = None
             self._length = 0
        current = elements._head
        while current:
            self.append(current.data)
            current = current.next