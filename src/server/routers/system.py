from fastapi import APIRouter, Response, status

system_router = APIRouter()

@system_router.get("/ping", tags=["System"])
async def ping(response: Response):
    response.status_code = status.HTTP_200_OK
