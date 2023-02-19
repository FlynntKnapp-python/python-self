# Notes

## New and/or Interesting Concepts

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
