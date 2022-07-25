from enum import Enum
from fastapi import status


class ErrorData:
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message


class AppErrors(Enum):
    UNEXPECTED = ErrorData(
        status.HTTP_400_BAD_REQUEST,
        'Unexpected error'
    )

    OPERATION_NOT_PERMITTED = ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Operation not permitted'
    )

    USER_NOT_FOUND = ErrorData(
        status.HTTP_404_NOT_FOUND,
        'User not found'
    )

    PROJECT_NOT_FOUND = ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Project not found'
    )

    DEVICE_NOT_FOUND = ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Device not found'
    )

    ATTRIBUTE_NOT_FOUND = ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Attribute not found'
    )

    READING_NOT_FOUND = ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Reading not found'
    )

    DUPLICATED_PROJECT_NAME = ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Duplicated project name'
    )

    DUPLICATED_DEVICE_NAME = ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Duplicated device name'
    )

    DUPLICATED_ATTRIBUTE_NAME = ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Duplicated attribute name'
    )

    MISSING_DEVICE_TOKEN = ErrorData(
        status.HTTP_401_UNAUTHORIZED,
        'Missing device authorization token'
    )

    INVALID_DEVICE_TOKEN = ErrorData(
        status.HTTP_401_UNAUTHORIZED,
        'Invalid device token'
    )

    INVALID_READING_VALUE = ErrorData(
        status.HTTP_400_BAD_REQUEST,
        'Invalid reading value'
    )

    NOT_AUTHORIZED_TO_CREATE_ATTRIBUTE_READING = ErrorData(
        status.HTTP_401_UNAUTHORIZED,
        'Not authorized to create a reading for the given attribute'
    )


class AppError(Exception):
    def __init__(self, error: AppErrors):
        super()
        self.error = error
