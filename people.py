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

# Define a `main` function to run some code in this file. TODO: Decide better verbiage.
def main():
    # Create a new `Person` instance with an argument of `"MyName"` and
    # assign it to the variable `me`.
    me = Person("MyName")
    # Call the `print_self` method on the `me` instance.
    me.print_self()

# If this file is run directly:
if __name__ == "__main__":
    # Run the `main` function, defined above.
    main()
