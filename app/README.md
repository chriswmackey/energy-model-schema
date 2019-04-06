# app folder structure

`main.py`: the main application. It starts the app and also customizes the `openapi` schema.

## Folders:

*api*: Includes documentation for all the endpoints.

*core*: Includes core functionalities such as errors, security and utilities.

*crud*: Includes all methods to create, read, update and delete resources. Group crud
methods for database, bucket, etc in separate files.

*db*: Includes database utilities to initialize, start and stop database.

*models*: Includes all object schemas including database models.
