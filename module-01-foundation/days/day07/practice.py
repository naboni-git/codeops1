import time
from collections import deque

# =====================================================================
# 1. Name the Big-O (Explaining with code comments)
# =====================================================================

# Snippet A: List Indexing
# Big-O: O(1) [Constant Time]
# Why: Accessing an element in an array/list using an index takes the 
# exact same amount of time, regardless of whether the list has 5 or 5,000,000 items.
names = ["Almaz", "Dawit", "Naboni"]
first_student = names[0]  # O(1)

# Snippet B: Single Loop
# Big-O: O(N) [Linear Time]
# Why: The loop runs exactly once for each item in the list. If the list length (N) doubles,
# the time it takes to run doubles.
for name in names:
    print(name)  # O(N)

# Snippet C: Nested Loop
# Big-O: O(N^2) [Quadratic Time]
# Why: For every item in the outer loop, we run the entire inner loop.
# If N is 10, it runs 10 * 10 = 100 times.
for i in range(len(names)):
    for j in range(len(names)):
        print(names[i], names[j])  # O(N^2)

# Snippet D: Dictionary Lookup
# Big-O: O(1) [Constant Time]
# Why: Python dictionaries use "hash tables," allowing instant lookup by key
# without scanning through the dictionary.
student_directory = {"SAV-101": "Naboni", "SAV-102": "Almaz"}
student = student_directory.get("SAV-101")  # O(1)

# Snippet E: Binary Search
# Big-O: O(log N) [Logarithmic Time]
# Why: Because the list is sorted, we split the search area in half on every step,
# finding the item incredibly fast.


# =====================================================================
# 2. List vs. Dict Lookup Performance Time Test
# =====================================================================
print("--- 2. List vs. Dict Lookup Time Test ---")
# Build a list and a dictionary of 100,000 items
max_items = 100000
test_list = [f"ACC{i}" for i in range(max_items)]
test_dict = {f"ACC{i}": i for i in range(max_items)}

target_key = "ACC99999"  # Element near the end of our structures

# Time the List Lookup (Linear Search - O(N))
start_time = time.perf_counter()
is_in_list = target_key in test_list
list_lookup_time = time.perf_counter() - start_time
print(f"List Lookup Time: {list_lookup_time:.6f} seconds (Result: {is_in_list})")

# Time the Dictionary Lookup (Hash Table - O(1))
start_time = time.perf_counter()
is_in_dict = target_key in test_dict
dict_lookup_time = time.perf_counter() - start_time
print(f"Dict Lookup Time: {dict_lookup_time:.6f} seconds (Result: {is_in_dict})")
print(f"Dictionary is {list_lookup_time / dict_lookup_time:.1f}x faster than List!")


# =====================================================================
# 3. Build a Stack (LIFO) to Reverse Names
# =====================================================================
print("\n--- 3. Reversing a List with a Stack ---")
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

# Reversing names using our Stack
name_stack = Stack()
original_names = ["Naboni", "Almaz", "Dawit", "Tigist"]
print("Original List:", original_names)

for name in original_names:
    name_stack.push(name)

reversed_names = []
while not name_stack.is_empty():
    reversed_names.append(name_stack.pop())

print("Reversed List:", reversed_names)


# =====================================================================
# 4. Build a Bank Queue (FIFO) using deque
# =====================================================================
print("\n--- 4. Bank Queue Service Line ---")
# We use collections.deque because appending and popping from ends is O(1)
bank_line = deque()

# Enqueue 5 customers
bank_line.append("Customer A")
bank_line.append("Customer B")
bank_line.append("Customer C")
bank_line.append("Customer D")
bank_line.append("Customer E")
print("Initial Line:", list(bank_line))

# Serve them in FIFO order (popleft)
while len(bank_line) > 0:
    served = bank_line.popleft()
    print(f"Serving: {served}. Customers remaining in queue: {len(bank_line)}")


# =====================================================================
# 5. Singly Linked List
# =====================================================================
print("\n--- 5. Singly Linked List Walk ---")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node in line

class LinkedList:
    def __init__(self):
        self.head = None  # The starting node of our chain

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new node to current head
        self.head = new_node  # Make this new node the new head

    def print_all(self):
        current = self.head
        chain = []
        while current is not None:
            chain.append(str(current.data))
            current = current.next
        print(" -> ".join(chain) + " -> None")

# Creating a linked list and testing it
my_list = LinkedList()
my_list.push_front("Dawit")
my_list.push_front("Almaz")
my_list.push_front("Naboni")
my_list.print_all()  # Prints: Naboni -> Almaz -> Dawit -> None