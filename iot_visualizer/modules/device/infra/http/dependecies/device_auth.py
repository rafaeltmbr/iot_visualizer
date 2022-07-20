from fastapi import Request

from ...sqlalchemy.repositories.DeviceRepository import DeviceRepository
from .....shared.providers.Auth.BasicAuth import BasicAuth
from .....shared.utils.AppError import AppError, ErrorType

def get_basic_credentials(req: Request):
    authorization = req.headers.get('authorization')

    if not authorization:
        raise AppError(ErrorType.MISSING_DEVICE_TOKEN)

    header_parts = authorization.split(' ')

    if len(header_parts) != 2:
        raise AppError(ErrorType.INVALID_DEVICE_TOKEN)

    user, password = BasicAuth.decode(header_parts[1])

    if not user or not password:
        raise AppError(ErrorType.INVALID_DEVICE_TOKEN)

    return user, password


def device_auth(req: Request):
    id, secret = get_basic_credentials(req)

    device = DeviceRepository().find_by_id(id)

    if not device:
        raise AppError(ErrorType.DEVICE_NOT_FOUND)

    if device.secret != secret:
        raise AppError(ErrorType.INVALID_DEVICE_TOKEN)

