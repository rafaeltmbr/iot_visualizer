import json
from typing import Union
from fastapi import Request, Response

from ....utils.AppError import AppError, ErrorType

def get_error_response(app_error: AppError, unexpected: Union[Exception, None] = None) -> Response:
    error_type = str(app_error.type).split('.')[1]

    content = json.dumps({
        "error": error_type,
        "message": str(unexpected) if unexpected else app_error.message,
    })

    return Response(content, status_code=app_error.status)


async def excepetion_middleware(req: Request, call_next):
    try:
        return await call_next(req)

    except AppError as e:
        return get_error_response(e)

    except Exception as e:
        return get_error_response(AppError(ErrorType.UNEXPECTED), e)
