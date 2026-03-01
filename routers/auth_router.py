from fastapi import APIRouter, Form, status, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import get_db
from auth_logic import add_user, verify_password
import models
from schemas import UserCreate, UserLogin, as_form


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
    credentials: UserLogin,
    db: Session = Depends(get_db)
):

    #! For now code with @ as first symbol is deleted
    #! If needed can be taken from previous commits in GitHub

    user: models.User = db.query(models.User).filter(
        or_(
            models.User.username == credentials.username_or_email,
            models.User.email == credentials.username_or_email
        )
    ).first()


    if not user or not verify_password(credentials.password, user.hashed_password): # type: ignore      #? Your IDE might be mad at user.hashed_password,
        return RedirectResponse(                                                                        #? but it's correct, so we i added "type: ignore" 
            url="/signin?error=invalid_credentials",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    print(f"User {user.username} logged in successfully!")

    return RedirectResponse(url=f"/chats/{user.id}", status_code=status.HTTP_303_SEE_OTHER)


#Opens "sign-up" page
@auth_router.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("sign-up.html", {"request": request})


# Actions after pressing send button in signin form
@auth_router.post("/signup")
async def handle_registration(
        user_data: UserCreate = Depends(as_form(UserCreate)),
        db: Session = Depends(get_db)
    ):

    # Transforms Pydentinc type object into dict that we can push into data base via add_user
    user_dict = user_data.model_dump(exclude={'confirm_password'})

    # Addes user to database
    add_user(db, user_dict)

    return RedirectResponse(url="/signin", status_code=status.HTTP_303_SEE_OTHER)
