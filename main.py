from fastapi import FastAPI, Form, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from database import engine, Base
import models
from routers import auth, chat


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create the database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def welcome_page():
    return FileResponse("templates/welcome.html")

@app.get("/signin")
async def signin_page():
    return FileResponse("templates/signin.html")

@app.get("/signup")
async def signup_page():
    return FileResponse("templates/signup.html")

@app.get("/chats")
async def chats_page():
    return FileResponse("templates/chats.html")

@app.get("/chat/{chat_id}")
async def chat_page(chat_id: int):
    return FileResponse("templates/chat.html")

@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return FileResponse("templates/404.html")


@app.post("/signup")
async def handle_registration(
    username_placeholder: str = Form(...),
    email_placeholder: str = Form(...),
    password_placeholder: str = Form(...),
    confirm_pasword: str = Form(...),
):

    print(f"New User: {username_placeholder}")
    print(f"New User's email: {email_placeholder}")
    print(f"New User's password: {password_placeholder}")

    return RedirectResponse(url="/chats", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/signin")
async def handle_signing_in(
    email_placeholder: str = Form(...),
    password_placeholder: str = Form(...),
):
    print(f"Email: {email_placeholder}")
    print(f"Password: {password_placeholder}")

    return RedirectResponse(url="/chats", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
