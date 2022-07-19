import json
from fastapi import Request, Response, status


async def execpetion_handler_middleware(req: Request, call_next):
    try:
        return await call_next(req)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status_code=status.HTTP_400_BAD_REQUEST)
