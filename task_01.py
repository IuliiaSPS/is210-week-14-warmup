#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


from pet import Pet


class Dog(Pet):
    """Object to inherit from Pet class."""
    def __init__(self, has_shots=False, **args):
        """Constructor for Dog class.

        Args:
            has_shots(bool, optional): If dog was vaccinated. Defult: False.
            *args(mixed): An arbitrary arguments dictionary.

        Attributes:
            has_shots(bool, optional): If dog was vaccinated. Defult: False.
            *args(mixed): An arbitrary arguments dictionary.
        """
        self.has_shots = has_shots
        super(Dog, self).__init__(**args)
