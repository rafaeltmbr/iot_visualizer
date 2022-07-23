import json
from typing import Union
from fastapi import Request, Response

from ....utils.AppError import AppError, AppErrors

def get_error_response(app_error: AppError, unexpected_message: Union[Exception, None] = None) -> Response:
    error_data = app_error.error.value

    content = json.dumps({
        "error": str(app_error.error).split('.')[1],
        "message": str(unexpected_message) if unexpected_message else error_data.message,
    })

    return Response(content, status_code=error_data.status)


async def excepetion_middleware(req: Request, call_next):
    try:
        return await call_next(req)

    except AppError as e:
        return get_error_response(e)

    except Exception as e:
        return get_error_response(AppError(AppErrors.UNEXPECTED), e)
