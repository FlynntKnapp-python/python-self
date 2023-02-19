class Person:
    """
    Class for a person.

    Attributes:
        name (str): The name of the person.
    """
    def __init__(self, user_provided_name):
        """
        Create an instance of `Person`. Set the `Person` instance `name`
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

me = Person("MyName")
me.print_self()
