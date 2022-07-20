from typing import NamedTuple


def update_instance_attributes(instance, attributes: NamedTuple, exclude_none: bool = False):
    for key, value in zip(attributes._fields, attributes):
        if exclude_none and value == None: continue

        setattr(instance, key, value)

    return instance