#!/usr/bin/python3
"""
Module 12-student
"""


class Student():
    """DEfine student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, string)
        for JSON serialization of an object
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student
        """
        for i in json:
            self.__dict__[i] = json[i]
