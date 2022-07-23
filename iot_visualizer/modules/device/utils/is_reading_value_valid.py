def is_valid_number(value: str):
    try:
        float(value)
        return True
    except:
        return False


def is_valid_boolean(value: str):
    return value == 'true' or value == 'false'


def is_valid_text(value: str):
    return True


validators = {
    'number': is_valid_number,
    'boolean': is_valid_boolean,
    'text': is_valid_text
}

def is_reading_value_valid(value: str, type: str):
    validator = validators.get(type, lambda v: False)

    return validator(value)
