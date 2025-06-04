Character = str

class InvalidIndexError(Exception):
    pass

class CharacterTypeError(Exception):
    pass

def is_character(element) -> bool:
    return isinstance(element, str) and len(element) == 1

class ListBasedList:
    def __init__(self, initial_data=None):
        self._data: list[Character] = []
        if initial_data:
            for item in initial_data:
                if is_character(item):
                    self._data.append(item)
                else:
                     raise CharacterTypeError(f"Initial data must contain only characters. Found: {item}")

    def __str__(self) -> str:
        return f"[{', '.join(repr(item) for item in self._data)}]"

    def __repr__(self) -> str:
        return f"ListBasedList({self._data!r})"

    def length(self) -> int:
        return len(self._data)

    def append(self, element: Character) -> None:
        if not is_character(element):
            raise CharacterTypeError(f"Can only append a single character string. Got: {element}")
        self._data.append(element)

    def insert(self, element: Character, index: int) -> None:
        if not is_character(element):
            raise CharacterTypeError(f"Can only insert a single character string. Got: {element}")
        if not (0 <= index <= self.length()):
             raise InvalidIndexError(f"Index {index} is out of bounds for insertion (0 to {self.length()})")
        self._data.insert(index, element)

    def delete(self, index: int) -> Character:
        if not (0 <= index < self.length()):
            raise InvalidIndexError(f"Index {index} is out of bounds for deletion (0 to {self.length() - 1})")
        return self._data.pop(index)

    def deleteAll(self, element: Character) -> None:
        if not is_character(element):
             return
        self._data = [item for item in self._data if item != element]

    def get(self, index: int) -> Character:
        if not (0 <= index < self.length()):
            raise InvalidIndexError(f"Index {index} is out of bounds (0 to {self.length() - 1})")
        return self._data[index]

    def clone(self) -> 'ListBasedList':
        return ListBasedList(self._data[:])

    def reverse(self) -> None:
        self._data.reverse()

    def findFirst(self, element: Character) -> int:
        if not is_character(element):
             return -1
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: Character) -> int:
        if not is_character(element):
             return -1
        for i in range(self.length() - 1, -1, -1):
            if self._data[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self._data = []

    def extend(self, elements: 'ListBasedList') -> None:
        if not isinstance(elements, ListBasedList):
             raise TypeError("Can only extend with another ListBasedList instance.")
        for item in elements._data:
            self.append(item)