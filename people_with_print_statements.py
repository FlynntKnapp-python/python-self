# 1. Create a `Person` class:
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
        print('self: ', self)
        print('Person: ', Person)
        print("user_provided_name: ", user_provided_name)
        print('isinstance(self, Person): ', isinstance(self, Person))
        self.name = user_provided_name
        print('self: ', self)

    def print_self(self):
        """
        Print the `Person` instance. `self` IS the current instance of `Person`.
        """
        print('self: ', self)

    # We are not defining __str__ here, so the default __str__ will be used.
    # def __str__(self):
    #     return self.name

# 2. Create an instance of `Person` with `name` attribute of `MyName`:
me = Person("MyName")
# 3. Call the `print_self` method on the `me` instance of `Person`:
me.print_self()
