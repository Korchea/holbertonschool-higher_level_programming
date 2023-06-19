#!/usr/bin/python3
"""
In this file I create a class MyList
"""


class MyList(list):
    """MyList

    Args:
        list (list): Is a list
    """

    def print_sorted(self):
        """print_sorted
        """
        sort_list = self.copy()
        sort_list = sorted(sort_list)
        print(sort_list)
