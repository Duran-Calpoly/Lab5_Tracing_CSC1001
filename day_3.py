"""CS 1001 Lab 5 - Day 3
References and aliasing.
"""

from typing import Optional


# Task 4 - Passing a List to a Function
def checked_access(values: list[int], idx: int) -> Optional[int]:
    test = idx >= 0 and idx < len(values)
    if test:
        return values[idx]
    else:
        return None


numbers = [1, 0, 1]
first = checked_access(numbers, 9)
second = checked_access(numbers, 2)

print(first)
print(second)


# Task 5 - References and Aliasing
first = [10, 20, 30]
second = first
third = second

print(first)
print(second)
print(third)


# Task 6 - Equal Values vs. Identical Objects
a = [4, 8, 12]
b = a
c = [4, 8, 12]
d = c

same_values = a == c
same_ab = a is b
same_ac = a is c

print(same_values)
print(same_ab)
print(same_ac)


# Task 7 - Aliasing Through Function Parameters
def first_value(values: list[int]) -> int:
    result = values[0]
    return result


numbers = [7, 4, 9]
answer = first_value(numbers)
print(answer)
