from fastapi import APIRouter

# Import separate routers using !absolute! paths
from routers.auth_router import auth_router
from routers.chats_router import chats_router
from ws_logic.chat_ws import ws_router

main_router = APIRouter()

# Combining routers into one
main_router.include_router(auth_router)
main_router.include_router(chats_router)
main_router.include_router(ws_router)
