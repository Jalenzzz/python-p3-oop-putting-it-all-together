#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand: str, size: int):
        self.brand = brand
        self.size = size
        self.condition = 'New'

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise ValueError("size must be an integer.")
        else:
            self._size = value

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = 'New'