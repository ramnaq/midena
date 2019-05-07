def remove_flag(flags, flag):
    if flags & flag:
        return flags ^ flag
    return flags
