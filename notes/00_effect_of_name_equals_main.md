# Effect of `__name__ == "__main__"` in `people.py`

## Debug Comparison

* Breakpoint at `me = people.Person(TEST_NAME_01)`:

  ![breakpoint](https://user-images.githubusercontent.com/47562501/221345418-d9626d46-3756-4612-afb1-c42cbf18ec0c.png)

### Without `__name__ == "__main__"`

* Debug panel variables:

  ![debug_panel_without_main_conditional](https://user-images.githubusercontent.com/47562501/221345851-7b512872-d2d2-4131-8227-9913b842c5ca.png)

* [`people.py`](../people.py):

  ```python
  #...
  me = Person("MyName")
  me.print_self()
  #...
  ```

### With `__name__ == "__main__"`

* Debug panel variables:

  ![debug_panel_with_main_conditional](https://user-images.githubusercontent.com/47562501/221345859-a25da11a-dbcc-4259-b78b-ffdd54de3593.png)

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
