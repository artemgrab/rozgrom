from fastapi import APIRouter, Form, status
from fastapi.responses import FileResponse, RedirectResponse


router = APIRouter()


@router.get("/chats")
async def chats_page():
    return FileResponse("templates/chats.html")

@router.get("/chat/{chat_id}")
async def chat_page(chat_id: int):
    return FileResponse("templates/chat.html")