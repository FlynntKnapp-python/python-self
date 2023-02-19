class Person:
    """
    Class for a person.
    """
    def __init__(self, name):
        self.name = name

    def print_self(self):
        print(self) # Put a breakpoint here and check the value of `self`.

    # We are not defining __str__ here, so the default __str__ will be used.
    # def __str__(self):
    #     return self.name


def main():
    me = Person("MyName")
    me.print_self()


if __name__ == "__main__":
    main()
