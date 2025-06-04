# Custom Typed List Implementation 

## Short Description

This application implements a custom typed list data structure, where elements are restricted to single characters (Character). The project demonstrates two different underlying implementations for the list: one based on Python's built-in list and another based on a doubly linked list. It includes a comprehensive set of operations such as adding, inserting, deleting, retrieving, searching, cloning, reversing, extending, and clearing the list, along with handling invalid inputs and indices.

## Variant Calculation and Description

My variant number is **3**.

According to the lab description based on the last digit of my student ID (variant 3), the requirements are:
- **Initial Implementation:** List based on Python's built-in arrays/lists (`list`).
- **Refactored Implementation:** Doubly Linked List.
- **Element Type:** Characters (single character strings).

Both implementations (`ListBasedList` and `DoublyLinkedList`) are designed to provide the same public interface, allowing for comparison and demonstrating different ways to achieve the same functionality.

## Instructions on How to Build and Run Tests

1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/turbososyn/mtrpz-lab2.git>
    cd mtrpz_lab2
    ```
2.  **Ensure Python is installed:**
    Make sure you have Python 3.9+ installed and accessible from your terminal. It's recommended to ensure `pip` is also correctly set up. If `python` or `pip` commands are not found, you might need to adjust your system's PATH or use `py -m` prefix as shown below.
3.  **Install pytest:**
    This project uses `pytest` for automated testing. Install it directly using pip:
    ```bash
    py -m pip install pytest
    ```
4.  **Run the tests:**
    Navigate to the root directory of the project in your terminal and execute pytest:
    ```bash
    py -m pytest
    ```
    Pytest will discover and run all tests defined in the `tests/` directory for both list implementations. A successful run will show green indicators for all collected tests.

## Link to Commit Where Tests Failed on CI
Failed CI tests commit: [`b1b0690`](https://github.com/turbososyn/quadratic_solver/commit/e1337d5a4da898348fc46816378378b38c811b2f)