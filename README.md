# Energy Model Schema

This repository extends Pollination model schema to support energy models.

## Requirements

Python `3.6` or higher.

## Usage

```shell
pip install -r requirements.txt
```

### Testing

For only testing energy model schemas try running

```console
python -m pytest --noconftest --ignore='tests\test_api.py' --ignore='tests\test_schema.py'
```

Run the command below to start the
application:

`uvicorn app.main:app --reload`

Try interactive API documentation at `http://127.0.0.1:8000/docs` to test the
application.

The redoc documentation is also generated from the endpoints and is available at: `http://127.0.0.1:8000/redoc`

### Extending Current Schema

1. Add you new Pydantic schemas for enrgy modeling to `app/models/energy`
2. Add a sample files for each schema to `app/models/samples`
3. Add new tests under `tests` folder. You can reuse the objects in sample files by importing them to your test module. See `test_schema_energy_construction.py` for an example.


### Export all samples as JSON files.

Run `python ./app/models/samples/samples_to_json.py` from the root directory. See `app/models/samples/json` for generated JSON files.
