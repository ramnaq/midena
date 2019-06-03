def remove_flag(flags, flag):
    if flags & flag:
        return flags ^ flag
    return flags


def is_into(element, listOfLists: list) -> bool:
    for L in listOfLists:
        if element in listOfLists:
            return True
    return False
