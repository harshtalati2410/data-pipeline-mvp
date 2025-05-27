from jsonschema import validate, ValidationError

def validate_data(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        raise ValueError(f"Validation failed: {e.message}")
