from enum import Enum
from fastapi import status


class ErrorData:
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message


class ErrorType(Enum):
    UNEXPECTED = 0
    OPERATION_NOT_PERMITTED = 1
    USER_NOT_FOUND = 2
    PROJECT_NOT_FOUND = 3
    DEVICE_NOT_FOUND = 4
    ATTRIBUTE_NOT_FOUND = 5
    READING_NOT_FOUND = 6
    DUPLICATED_PROJECT_NAME = 7
    DUPLICATED_DEVICE_NAME = 8
    DUPLICATED_ATTRIBUTE_NAME = 9


app_errors: dict[ErrorType, ErrorData] = {
    ErrorType.UNEXPECTED: ErrorData(
        status.HTTP_400_BAD_REQUEST,
        'Unexpected error'
    ),
    ErrorType.USER_NOT_FOUND: ErrorData(
        status.HTTP_404_NOT_FOUND,
        'User not found'
    ),
    ErrorType.PROJECT_NOT_FOUND: ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Project not found'
    ),
    ErrorType.DEVICE_NOT_FOUND: ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Device not found'
    ),
    ErrorType.ATTRIBUTE_NOT_FOUND: ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Attribute not found'
    ),
    ErrorType.READING_NOT_FOUND: ErrorData(
        status.HTTP_404_NOT_FOUND,
        'Reading not found'
    ),
    ErrorType.DUPLICATED_PROJECT_NAME: ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Duplicated project name'
    ),
    ErrorType.DUPLICATED_DEVICE_NAME: ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Duplicated device name'
    ),
    ErrorType.DUPLICATED_ATTRIBUTE_NAME: ErrorData(
        status.HTTP_403_FORBIDDEN,
        'Duplicated attribute name'
    ),
}


class AppError(Exception):
    def __init__(self, type: ErrorType):
        super()
        self.type = type
        self.status = app_errors[type].status
        self.message = app_errors[type].message
