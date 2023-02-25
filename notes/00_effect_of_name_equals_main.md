# Effect of `__name__ == "__main__"` in `people.py`

## Debug Comparison

* Breakpoint at `me = people.Person(TEST_NAME_01)`:
  * IMAGE_HERE

### Without `__name__ == "__main__"`

* Debug panel variables:
  * IMAGE_HERE

* [`people.py`](../people.py):

  ```python
  #...
  me = Person("MyName")
  me.print_self()
  #...
  ```

### With `__name__ == "__main__"`

* Debug panel variables:
  * IMAGE_HERE

* [`people.py`](../people.py):

  ```python
  #...
  def main():
      me = Person("MyName")
      me.print_self()

  if __name__ == "__main__":
      main()
  #...
  ```
