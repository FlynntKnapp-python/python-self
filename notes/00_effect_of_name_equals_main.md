# Effect of `__name__ == "__main__"` in `people.py`

## Debug Comparison

* Breakpoint at `me = people.Person(TEST_NAME_01)`:

  ![breakpoint](https://user-images.githubusercontent.com/47562501/221345418-d9626d46-3756-4612-afb1-c42cbf18ec0c.png)

### Without `__name__ == "__main__"`

* Debug panel variables:

  ![debug_panel_without_main_conditional](https://user-images.githubusercontent.com/47562501/221345541-dbf8a702-4c38-4fed-ab7c-78d415914c27.png)

* [`people.py`](../people.py):

  ```python
  #...
  me = Person("MyName")
  me.print_self()
  #...
  ```

### With `__name__ == "__main__"`

* Debug panel variables:

  ![debug_panel_with_main_conditional](https://user-images.githubusercontent.com/47562501/221345552-dfe9cadc-e3df-4d7b-87ed-49856290ea67.png)

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
