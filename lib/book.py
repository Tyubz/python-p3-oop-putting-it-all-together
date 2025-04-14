#!/usr/bin/env python3

class Book:
    def __init__(self, title="Unknown",page_count=0):
        self.title = title
        self.page_count = page_count
    def set_page_count(self, value):
        if isinstance(value, int):
            self.page_count = value
        else:
            print("page_count must be an integer\n")
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

