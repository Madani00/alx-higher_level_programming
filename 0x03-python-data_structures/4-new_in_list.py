#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace an element in a list without modifying the original list"""
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_newlist = my_list.copy()
    my_newlist[idx] = element
    return (my_newlist)
