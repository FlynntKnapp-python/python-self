# 1. Create a `Person` class:
class Person:
    """
    Class for a person.

    Attributes:
        name (str): The name of the person.
    """
    def __init__(self, user_provided_name):
        """
        Create an instance of `Person`. Set the `Person` instance `name` attribute to the
        argument provided as `user_provided_name`.
        """
        # Every variable, method, attribute, etc. in Python is an object
            # and has to be defined somewhere.
        # The `self` variable is a reference to the current instance of
            # the class.
        # We are defining a `name` attribute on the current instance of
            # `Person` and setting it to the value of the `user_provided_name`
            # argument.
        self.name = user_provided_name # Put a breakpoint here and check the value of `self`.
        pass

    def print_self(self):
        """
        Print the `Person` instance. `self` IS the current instance of `Person`.
        """
        print(self) # Put a breakpoint here and check the value of `self`.

    # We are not defining __str__ here, so the default __str__ will be used.
    # def __str__(self):
    #     return self.name

# 2. Create an instance of `Person` with `name` attribute of `MyName`:
me = Person("MyName")
# 3. Call the `print_self` method on the `me` instance of `Person`:
me.print_self()
