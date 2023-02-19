# Python `class`' `self`

## Resources

## Description

## `.gitignore`

* [gitignore generator](https://www.toptal.com/developers/gitignore/)

## Notes

* Demonstrate the output of `print(self)` in two scenarios:
  * When `__str__` is defined
  * When `__str__` is not defined

* Demonstrate how to find `__name__`

## New and/or Interesting Concepts

* `launch.json`:
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