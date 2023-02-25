import people

TEST_NAME_01 = "Name01"


def test_person():
    """
    Test that a `Person` instance is created with the correct name.

    * This test is checking the `Person` class `__init__` method.
    * We wrote the `__init__` method to take a `user_provided_name`
    argument and set it's value to the `Person` instance `name` attribute.
    """
    me = people.Person(TEST_NAME_01)
    assert me.name == TEST_NAME_01
