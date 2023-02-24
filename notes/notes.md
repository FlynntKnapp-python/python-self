# Notes

## New and/or Interesting Concepts

### `ImportError: attempted relative import with no known parent package`

#### The Error

* [`test_people.py`](../test_people.py)

  ```python
  from . import people
  ```

* `ImportError`

  ```bash
  test_people.py:1: in <module>
      from . import people
  E   ImportError: attempted relative import with no known parent package
  ```

* I suspect that we need to set the directory as a package, include a `__init__.py` file, and then import the module.

#### The Solution

* [`test_people.py`](../test_people.py)

  ```python
  import people
  ```

### `launch.json`

* Current File:

  ```json
  {
      // Use IntelliSense to learn about possible attributes.
      // Hover to view descriptions of existing attributes.
      // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
      "version": "0.2.0",
      "configurations": [
          {
              "name": "Python: Current File",
              "type": "python",
              "request": "launch",
              "program": "${file}",
              "console": "integratedTerminal",
              "justMyCode": true
          }
      ]
  }
  ```

* Specific File:

  ```json
  {
      // Use IntelliSense to learn about possible attributes.
      // Hover to view descriptions of existing attributes.
      // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
      "version": "0.2.0",
      "configurations": [
          {
              "name": "Python: people.py",
              "type": "python",
              "request": "launch",
              "program": "./people.py",
              "console": "integratedTerminal",
              "justMyCode": true
          }
      ]
  }
  ```

### VS Code Workspace Settings

* [Workspace settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings)
* [Multi-Root Workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces#_settings)
