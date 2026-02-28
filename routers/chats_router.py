from fastapi import APIRouter
from fastapi.responses import FileResponse


chats_router = APIRouter()


@chats_router.get("/chats/{user_id}")
async def chats_page():
    return FileResponse("templates/chats.html")


# Idk if this is the best way to do it, so if anyone has better idea write about it
# I'm talking about storing both ids in url like this /chat/{user_id}/{chat_id}
@chats_router.get("/chat/{user_id}/{chat_id}")
async def chat_page(chat_id: int):
    return FileResponse("templates/chat.html")
