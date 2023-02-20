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

  ![Debug view of self, and python class __init__ code before name assignment](https://user-images.githubusercontent.com/47562501/220025404-3898066d-4433-4e3e-80e1-1b623a5c5a46.png)

  ![Debug view of self before name assignment](https://user-images.githubusercontent.com/47562501/220025796-e2a9c8e5-1bb8-44fa-9417-4b93d9b17c5c.png)

  ![Debug view of self, and python class __init__ code after name assignment](https://user-images.githubusercontent.com/47562501/220026242-7bacecf3-c905-4953-ad16-782f5e19e288.png)

  ![Debug view of self after name assignment](https://user-images.githubusercontent.com/47562501/220026638-9e0f40c2-27a4-41c8-8a1a-9249054192f3.png)

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
