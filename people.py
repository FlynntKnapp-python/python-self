class Person:
    """
    Class for a person.

    Attributes:
        name (str): The name of the person.
    """
    def __init__(self, user_provided_name):
        """
        When a new `Person` is created, set the `Person` instance `name`
        attribute to the argument provided as `user_provided_name`.
        """
        self.name = user_provided_name
        pass

    def print_self(self):
        """
        Print the `Person` instance. `self` IS the current instance of
        `Person`.
        """
        print(self)

def main():
    me = Person("MyName")
    me.print_self()

if __name__ == "__main__":
    main()
