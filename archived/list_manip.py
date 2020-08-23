def list_manipulation(list, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3, 4]

        >>> list_manipulation(lst, 'remove', 'end')
        4

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [3]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3, 4]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3, 4]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 4, 30]

        >>> lst
        [20, 1, 2, 3, 4, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
#My Solution:

    if command == 'remove' and location == 'beginning':
        return list.pop(0),
    elif command == 'remove' and location == 'end':
        return list.pop(-1),
    elif command == 'add' and location == 'beginning':
        list.insert(0, value),
        return list,
    elif command == 'add' and location == 'end':
        list.append(value),
        return list
    else:
        return 'none'



# -----------------------------------------------------
# school solution 

    # if command == "remove":
    #     if location == "end":
    #         return list.pop()
    #     elif location == "beginning":
    #         return list.pop(0)

    # elif command == "add":
    #     if location == "beginning":
    #         list.insert(0, value)
    #         return list
    #     elif location == "end":
    #         list.append(value)
    #         return list

print(list_manipulation([1,2,3,4], 'remove', 'end'))
print(list_manipulation([1,2,3,4], 'remove', 'beginning'))
print(list_manipulation([1,2,3,4], 'add', 'end', 10))
print(list_manipulation([1,2,3,4], 'add', 'beginning', 30))
print(list_manipulation([1,2,3,4], 'foo', 'end'))
