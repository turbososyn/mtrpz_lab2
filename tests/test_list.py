import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import pytest

from common_definitions import Character, InvalidIndexError, CharacterTypeError, is_character
from list_based_impl import ListBasedList
from src.doubly_linked_impl import DoublyLinkedList

@pytest.fixture(params=[ListBasedList, DoublyLinkedList])
def empty_char_list(request):
    list_type = request.param
    return list_type()

@pytest.fixture(params=[ListBasedList, DoublyLinkedList])
def populated_char_list(request):
    list_type = request.param
    initial_data = ['A', 'B', 'C', 'A', 'D', 'B']
    return list_type(initial_data)

def test_length(empty_char_list, populated_char_list):
    assert empty_char_list.length() == 0
    assert populated_char_list.length() == 6

def test_append(empty_char_list):
    empty_char_list.append('X')
    assert empty_char_list.length() == 1
    assert empty_char_list.get(0) == 'X'

    empty_char_list.append('Y')
    assert empty_char_list.length() == 2
    assert empty_char_list.get(1) == 'Y'

    with pytest.raises(CharacterTypeError):
        empty_char_list.append("TooLong")
    with pytest.raises(CharacterTypeError):
        empty_char_list.append(123)

def test_insert(empty_char_list, populated_char_list):
    with pytest.raises(InvalidIndexError):
        empty_char_list.insert('A', -1)
    with pytest.raises(InvalidIndexError):
        empty_char_list.insert('A', 1)

    empty_char_list.insert('Z', 0)
    assert empty_char_list.length() == 1
    assert empty_char_list.get(0) == 'Z'

    empty_char_list.insert('W', 1)
    assert empty_char_list.length() == 2
    assert empty_char_list.get(1) == 'W'
    assert str(empty_char_list) == "['Z', 'W']"

    original_populated_str = str(populated_char_list)

    populated_char_list.insert('X', 0)
    assert populated_char_list.length() == 7
    assert populated_char_list.get(0) == 'X'
    assert str(populated_char_list) == "['X', 'A', 'B', 'C', 'A', 'D', 'B']"

    populated_char_list.insert('M', 3)
    assert populated_char_list.length() == 8
    assert str(populated_char_list) == "['X', 'A', 'B', 'M', 'C', 'A', 'D', 'B']"

    populated_char_list.insert('Y', populated_char_list.length())
    assert populated_char_list.length() == 9
    assert populated_char_list.get(8) == 'Y'
    assert str(populated_char_list) == "['X', 'A', 'B', 'M', 'C', 'A', 'D', 'B', 'Y']"

    with pytest.raises(InvalidIndexError):
         populated_char_list.insert('A', -1)
    with pytest.raises(InvalidIndexError):
         populated_char_list.insert('A', populated_char_list.length() + 1)

    with pytest.raises(CharacterTypeError):
        populated_char_list.insert("TooLong", 0)
    with pytest.raises(CharacterTypeError):
        populated_char_list.insert(123, 1)

def test_delete(populated_char_list):
    original_length = populated_char_list.length()

    deleted_char = populated_char_list.delete(2)
    assert deleted_char == 'C'
    assert populated_char_list.length() == original_length - 1
    assert str(populated_char_list) == "['A', 'B', 'A', 'D', 'B']"

    deleted_char = populated_char_list.delete(0)
    assert deleted_char == 'A'
    assert populated_char_list.length() == original_length - 2
    assert str(populated_char_list) == "['B', 'A', 'D', 'B']"

    deleted_char = populated_char_list.delete(populated_char_list.length() - 1)
    assert deleted_char == 'B'
    assert populated_char_list.length() == original_length - 3
    assert str(populated_char_list) == "['B', 'A', 'D']"

    while populated_char_list.length() > 0:
        populated_char_list.delete(0)

    assert populated_char_list.length() == 0
    assert str(populated_char_list) == "[]"

    with pytest.raises(InvalidIndexError):
        populated_char_list.delete(0)
    with pytest.raises(InvalidIndexError):
        populated_char_list.delete(-1)

    temp_list = populated_char_list.__class__(['Z'])
    with pytest.raises(InvalidIndexError):
        temp_list.delete(1)
    with pytest.raises(InvalidIndexError):
        temp_list.delete(-1)

def test_deleteAll(populated_char_list):
    populated_char_list.deleteAll('A')
    assert populated_char_list.length() == 4
    assert str(populated_char_list) == "['B', 'C', 'D', 'B']"

    populated_char_list.deleteAll('C')
    assert populated_char_list.length() == 3
    assert str(populated_char_list) == "['B', 'D', 'B']"

    populated_char_list.deleteAll('B')
    assert populated_char_list.length() == 1
    assert str(populated_char_list) == "['D']"

    populated_char_list.deleteAll('D')
    assert populated_char_list.length() == 0
    assert str(populated_char_list) == "[]"

    populated_char_list.deleteAll('Z')
    assert populated_char_list.length() == 0
    assert str(populated_char_list) == "[]"

    populated_char_list = populated_char_list.__class__(['1', '2', '3'])
    populated_char_list.deleteAll('Z')
    assert populated_char_list.length() == 3
    assert str(populated_char_list) == "['1', '2', '3']"

    populated_char_list.deleteAll(123)
    assert populated_char_list.length() == 3

def test_get(populated_char_list):
    assert populated_char_list.get(0) == 'A'
    assert populated_char_list.get(1) == 'B'
    assert populated_char_list.get(2) == 'C'
    assert populated_char_list.get(3) == 'A'
    assert populated_char_list.get(4) == 'D'
    assert populated_char_list.get(5) == 'B'

    with pytest.raises(InvalidIndexError):
        populated_char_list.get(-1)
    with pytest.raises(InvalidIndexError):
        populated_char_list.get(6)

    empty_list = populated_char_list.__class__()
    with pytest.raises(InvalidIndexError):
        empty_list.get(0)

def test_clone(populated_char_list):
    cloned_list = populated_char_list.clone()

    assert cloned_list is not populated_char_list

    assert str(cloned_list) == str(populated_char_list)
    assert cloned_list.length() == populated_char_list.length()

    if cloned_list.length() > 0:
        original_str_before_clone_modify = str(populated_char_list)
        cloned_list.delete(0)
        assert cloned_list.length() == populated_char_list.length() - 1
        assert str(populated_char_list) == original_str_before_clone_modify

    empty_list = populated_char_list.__class__()
    cloned_empty_list = empty_list.clone()
    assert cloned_empty_list is not empty_list
    assert cloned_empty_list.length() == 0
    assert str(cloned_empty_list) == "[]"

def test_reverse(populated_char_list):
    populated_char_list.reverse()
    assert str(populated_char_list) == "['B', 'D', 'A', 'C', 'B', 'A']"
    assert populated_char_list.length() == 6

    populated_char_list.reverse()
    assert str(populated_char_list) == "['A', 'B', 'C', 'A', 'D', 'B']"
    assert populated_char_list.length() == 6

    empty_list = populated_char_list.__class__()
    empty_list.reverse()
    assert empty_list.length() == 0
    assert str(empty_list) == "[]"

    single_list = populated_char_list.__class__(['Z'])
    single_list.reverse()
    assert single_list.length() == 1
    assert str(single_list) == "['Z']"

def test_findFirst(populated_char_list):
    assert populated_char_list.findFirst('A') == 0
    assert populated_char_list.findFirst('B') == 1
    assert populated_char_list.findFirst('C') == 2
    assert populated_char_list.findFirst('D') == 4
    assert populated_char_list.findFirst('Z') == -1

    empty_list = populated_char_list.__class__()
    assert empty_list.findFirst('A') == -1

    assert populated_char_list.findFirst(123) == -1

def test_findLast(populated_char_list):
    assert populated_char_list.findLast('A') == 3
    assert populated_char_list.findLast('B') == 5
    assert populated_char_list.findLast('C') == 2
    assert populated_char_list.findLast('D') == 4
    assert populated_char_list.findLast('Z') == -1

    empty_list = populated_char_list.__class__()
    assert empty_list.findLast('A') == -1

    assert populated_char_list.findLast(123) == -1

def test_clear(populated_char_list):
    populated_char_list.clear()
    assert populated_char_list.length() == 0
    assert str(populated_char_list) == "[]"

    populated_char_list.clear()
    assert populated_char_list.length() == 0
    assert str(populated_char_list) == "[]"

def test_extend(populated_char_list):
    original_length = populated_char_list.length()

    other_list = populated_char_list.__class__(['X', 'Y', 'Z'])

    populated_char_list.extend(other_list)
    assert populated_char_list.length() == original_length + other_list.length()
    assert str(populated_char_list) == "['A', 'B', 'C', 'A', 'D', 'B', 'X', 'Y', 'Z']"

    assert str(other_list) == "['X', 'Y', 'Z']"

    other_list.append('W')
    assert str(other_list) == "['X', 'Y', 'Z', 'W']"
    assert str(populated_char_list) == "['A', 'B', 'C', 'A', 'D', 'B', 'X', 'Y', 'Z']"

    empty_other_list = populated_char_list.__class__()
    populated_char_list.extend(empty_other_list)
    assert empty_other_list.length() == 0
    assert str(populated_char_list) == "['A', 'B', 'C', 'A', 'D', 'B', 'X', 'Y', 'Z']"

    empty_list = populated_char_list.__class__()
    empty_list.extend(other_list)
    assert empty_list.length() == 4
    assert str(empty_list) == "['X', 'Y', 'Z', 'W']"

    with pytest.raises(TypeError):
         populated_char_list.extend([1, 2, 3])

def test_initialization_with_invalid_data(empty_char_list):
    list_type = empty_char_list.__class__
    with pytest.raises(CharacterTypeError):
        list_type(['A', 'B', 123, 'D'])

    with pytest.raises(CharacterTypeError):
        list_type(['A', "TooLong", 'C'])