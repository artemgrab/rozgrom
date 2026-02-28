from fastapi import APIRouter

from .auth_router import auth_router
from .chats_router import chats_router

main_router = APIRouter()


main_router.include_router(auth_router)
main_router.include_router(chats_router)
