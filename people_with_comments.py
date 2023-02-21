# 1. Create a `Person` class:
class Person:
    """
    Class for a person.

    Attributes:
        name (str): The name of the person.
    """
    def __init__(this_specific_instance, user_provided_name):
        """
        Create an instance of `Person`. Set the `Person` instance `name`
        attribute to the argument provided as `user_provided_name`.

        We are replacing the usual 'self' with 'this_specific_instance'
        to make it clear that the first argument of the method is not a
        keyword, but a variable name for the current instance that doesn't
        have to be 'self'.

        This instance-specific variable name can be used throughout the
        methods which are part of the class.
        """
        # Every variable, method, attribute, etc. in Python is an object
            # and has to be defined somewhere.
        # The `this_specific_instance` variable is a reference to the
            # current instance (object) of the class.
        # We are defining a `name` attribute on the current instance of
            # `Person` and setting it to the value of the `user_provided_name`
            # argument.
        this_specific_instance.name = user_provided_name # Put a breakpoint here and check the value of `this_specific_instance`.
        pass

    def print_self(still_this_specific_instance):
        """
        Print the `Person` instance. `still_this_specific_instance` IS the current instance of `Person`.
        """
        print(still_this_specific_instance) # Put a breakpoint here and check the value of `this_specific_instance`.

    # We are not defining __str__ here, so the default __str__ will be used.
    # def __str__(this_specific_instance):
    #     return this_specific_instance.name

# 2. Create an instance of `Person` with `name` attribute of `MyName`:
me = Person("MyName")
# 3. Call the `print_self` method on the `me` instance of `Person`:
me.print_self()
