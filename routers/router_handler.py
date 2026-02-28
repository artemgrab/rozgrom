from fastapi import APIRouter

<<<<<<< HEAD
from .auth_router import auth_router
from .chats_router import chats_router

main_router = APIRouter()


=======
# Import separate routers using !absolute! paths
from routers.auth_router import auth_router
from routers.chats_router import chats_router
from ws_logic.chat_ws import ws_router

main_router = APIRouter()

# Combining routers into one
>>>>>>> 58154a785fc562a8615c152f1e4d74686d2998bf
main_router.include_router(auth_router)
main_router.include_router(chats_router)
main_router.include_router(ws_router)
