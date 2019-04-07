# Model Service

This is the bare minimum for model service built using `FastAPI` and `SQLAlchemy`.

The schemas are set using `pydantic` and with the magic of `FastAPI` the validation of
request and responses happens automatically with no need to write extra code.

It also generates the `openapi` documentation based on the endpoints and schemas. See below.

## Requirements

Python `3.6` or higher.

## Usage

```shell
pip install -r requirements.txt
```

For local test you need a JWT token to authorize your calls. You can use the code below
to generate a valid Token based on default values. You can use this JWT token for your
tests:

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcl9pZCI6IjY3ZDdlNjg3LWRkNGYtNGZlMC1iMWVlLWMyOWJmNzczZDk0NCIsIm5hbWUiOiJ0ZXN0X3VzZXIiLCJpYXQiOjE1MTYyMzkwMjJ9.UzO8oEKvYeI-AFRJ6tH5xxntP2jMmRn8wr_sWL6YE_4`

It contains the following payload:

```json
{
  "sub": "1234567890",
  "user_id": "67d7e687-dd4f-4fe0-b1ee-c29bf773d944",
  "name": "test_user",
  "iat": 1516239022
}
```

### Testing
For testing purposes you must export this environment variable:
```console
export POSTGRES_DB=test
```

You should then be able to run pytest without any issues in the root of this project like so:

```console
python -m pytest
```

**IMPORTANT SECURITY NOTE**

_In Pollination validation is handled by [Istio](https://istio.io/) and each
micro-service only decodes the token without validation. If you want to use this
micro-service also as a source of authorization/ validation then you need to rewrite the
jwt and security parts. See FastAPI documentation for more information on how you can set
it up._


You also need to create a new database named `pollination`. The default username and
password are both set to `postgres`. You can change all these values in `.env` file.

![image](https://user-images.githubusercontent.com/2915573/55664928-6e96c980-5804-11e9-84f1-238fbbadeeeb.png)

Once you have created the database you can create all the table schemas by running the following command from the root folder of this project:
```console
alembic upgrade head
```

Once you have the database set-up successfully run the command below to start the
application:

`uvicorn app.main:app --reload`

Try interactive API documentation at `http://127.0.0.1:8000/docs` to test the
application. Use jwt_token to authorize yourself.

![image](https://user-images.githubusercontent.com/2915573/55664937-9a19b400-5804-11e9-97c2-e88aa4ed07f8.png)

The redoc documentation is also generated from the endpoints and is available at: `http://127.0.0.1:8000/redoc`

<!-- ![sensor_grid_redoc](https://user-images.githubusercontent.com/2915573/55664978-55dae380-5805-11e9-9aa7-89d7660c67dd.gif) -->

## Credits

Developing this app was only possible with the help from the tutorials and the code from
these repositories:

[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/intro/)

[FastAPI real world example
app](https://github.com/nsidnev/fastapi-realworld-example-app)
