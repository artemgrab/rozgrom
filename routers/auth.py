from fastapi import APIRouter, Form, status
from fastapi.responses import FileResponse, RedirectResponse


router = APIRouter()


@router.get("/")
async def welcome_page():
    return FileResponse("templates/welcome.html")


@router.get("/signin")
async def signin_page():
    return FileResponse("templates/signin.html")

@router.post("/signin")
async def handle_signing_in(
    email_placeholder: str = Form(...),
    password_placeholder: str = Form(...),
):

    return RedirectResponse(url="/chats", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/signup")
async def signup_page():
    return FileResponse("templates/signup.html")

@router.post("/signup")
async def handle_registration(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
):

    #! One of future implementations
    # if len(password) > 71: return {"error": "Password shouldn't be longer than 71 cahracters"}
    # elif len(password) < 8: return {"error": "Password should be at least 8 long"}
    
    return RedirectResponse(url="/chats", status_code=status.HTTP_303_SEE_OTHER)