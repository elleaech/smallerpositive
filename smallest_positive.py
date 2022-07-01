from sys import exit
from typing import List


def DEBUG(msg):
    print(msg)


def smallest_positive(list_of_numbers: List[int]):
    list_of_numbers.sort()

    smaller_number = 1

    for list_number in list_of_numbers:
        DEBUG("%d, %d" % (list_number, smaller_number))

        if list_number == smaller_number:
            smaller_number += 1

    return smaller_number


if __name__ == "__main__":
    given_list = [3, 4, -1, 1]

    print("Smaller positive number (not present): %d" % smallest_positive(given_list))

    exit(0)
