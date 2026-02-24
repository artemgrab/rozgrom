from fastapi import APIRouter, Form, status, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Tells FastAPI where html files are
templates = Jinja2Templates(directory="templates")


# Opens "welcome" page
@router.get("/")
async def welcome_page(request: Request):
    return templates.TemplateResponse("welcomeToDuplo.html", {"request": request})


# Opens "sign-in" page
@router.get("/signin")
async def signin_page(request: Request):
    return templates.TemplateResponse("sign-in.html", {"request": request})

@router.post("/signin")
async def handle_signing_in(
    email: str = Form(...),
    password: str = Form(...),
):
    
    print("Works correctly")
    
    return RedirectResponse(url="/chats", status_code=status.HTTP_303_SEE_OTHER)


# Opens "sign-up" page
@router.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("sign-up.html", {"request": request})

@router.post("/signup")
async def handle_registration(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
):

    print("Works correctly")

    #! One of future implementations
    # if len(password) > 71: return {"error": "Password shouldn't be longer than 71 cahracters"}
    # elif len(password) < 8: return {"error": "Password should be at least 8 long"}
    
    return RedirectResponse(url="/signin", status_code=status.HTTP_303_SEE_OTHER)