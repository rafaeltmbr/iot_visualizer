from enum import Enum
from fastapi import status


class ErrorData:
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message


class ErrorType(Enum):
    UNEXPECTED = 0
    USER_NOT_FOUND = 1
    PROJECT_NOT_FOUND = 2
    DEVICE_NOT_FOUND = 3
    ATTRIBUTE_NOT_FOUND = 4
    READING_NOT_FOUND = 5


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
}


class AppError(Exception):
    def __init__(self, type: ErrorType):
        super()
        self.type = type
        self.status = app_errors[type].status
        self.message = app_errors[type].message
