from fastapi import APIRouter, Form, status, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from auth_logic import add_user
import models


auth_router = APIRouter()

# Tells FastAPI where html files are
templates = Jinja2Templates(directory="templates")


# Opens "welcome" page
@auth_router.get("/")
async def welcome_page(request: Request):
    return templates.TemplateResponse("welcomeToDuplo.html", {"request": request})


# Opens "sign-in" page
@auth_router.get("/signin")
async def signin_page(request: Request):
    return templates.TemplateResponse("sign-in.html", {"request": request})


# Actions after pressing send button in signin form
@auth_router.post("/signin")
async def handle_signing_in(
    username_or_email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):

    if username_or_email.startswith("@"):
        user = (
            db.query(models.User)
            .filter(models.User.username == username_or_email)
            .first()
        )
    else:
        user = (
            db.query(models.User).filter(models.User.email == username_or_email).first()
        )

    if not user:
        return RedirectResponse(
            url="/signin?error=user_not_found",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    if not verify_password(password, user.hashed_password):
        return RedirectResponse(
            url="/signin?error=invalid_credentials",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    print(f"User {user.username} logged in successfully!")

    return RedirectResponse(
        url=f"/chats/{user.id}", status_code=status.HTTP_303_SEE_OTHER
    )


# Opens "sign-up" page
@auth_router.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("sign-up.html", {"request": request})


# Actions after pressing send button in signin form
@auth_router.post("/signup")
async def handle_registration(
    full_name: str = Form(...),
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db),
):

    user_data = {
        "full_name": full_name,
        "username": username,
        "email": email,
        "password": password
    }

    if len(password) > 71:
        return RedirectResponse(
            url="/signup?error=password_is_too_long",
            status_code=status.HTTP_303_SEE_OTHER,
        )
    elif len(password) < 4:             # Changed to 4 characters for easier production
                                        # Change back to 8 characters after production
        return RedirectResponse(
            url="/signup?error=password_is_too_short",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    if password != confirm_password:
        return RedirectResponse(
            url="/signup?error=passwords_dont_match",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # Addes user to database
    add_user(db, user_data)


    return RedirectResponse(
        url="/chats/{user.id}", status_code=status.HTTP_303_SEE_OTHER
    )


    # TODO: Pydantic validator logic
