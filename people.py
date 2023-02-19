class Person:
    """
    Class for a person.
    """
    def __init__(self, name):
        self.name = name

    def print_self(self):
        print(self)

    # def __str__(self):
    #     return self.name


def main():
    me = Person("My Name")
    me.print_self()
    # <__main__.Person object at 0x0000023C068F9990>


if __name__ == "__main__":
    main()
