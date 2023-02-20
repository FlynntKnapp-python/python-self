# Python `class`' `self`

## Purpose

* Demonstrate what `self` is in a `class`
* Demonstrate how to use `self` in a `class`
* Demonstrate general investigation techniques:
  * Demonstrate how to check attributes of a Python object
    * Demonstrate how to check the attributes of `self`
    * What is `self`

## Examples

* Example without comments:
  * [`people.py`](./people.py)
* Example with comments:
  * [`people_with_comments.py`](./people_with_comments.py)
* Example with print statements:
  * [`people_with_print_statements.py`](./people_with_print_statements.py)

## Code with DEBUG Images

* Images:

  ![Before name assignment](./local_things\before_name_assignment.png)

  ![Degub view before assignment of name attribute](./local_things\self_before_name_assignment.png)

  ![After name assignment](./local_things\after_name_assignment.png)

  ![Degub view after assignment of name attribute](./local_things\self_after_name_assignment.png)

## Resources

### Keywords

* `def`
* `class`
* [`pass` - www.w3schools.com](https://www.w3schools.com/python/ref_keyword_pass.asp)

### Methods

* [`isinstance()` - www.w3schools.com](https://www.w3schools.com/python/ref_func_isinstance.asp)
* [`__init__()` - www.w3schools.com](https://www.w3schools.com/python/gloss_python_class_init.asp)
* `__str__()`

## Concepts

* Demonstrate how to find dunder attributes and methods:
  * `__name__`
  * `__str__`

* `<__main__.Person object at 0x0000023C068F9990>`:
  * What is default `__str__`?
  * What is `<>`?
  * What is `__main__`?
  * What is `Person`?
  * What is `0x0000023C068F9990`?

## Possible Improvements

* Is `user_provided_name` a good argument identifier?
  * Does is convey what it is better than using only `name`?
