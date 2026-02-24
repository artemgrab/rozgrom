from fastapi import APIRouter
from fastapi.responses import FileResponse


chats_router = APIRouter()


@chats_router.get("/chats")
async def chats_page():
    return FileResponse("templates/chats.html")


@chats_router.get("/chat/{chat_id}")
async def chat_page(chat_id: int):
    return FileResponse("templates/chat.html")
