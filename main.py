from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def signin_page():
    return FileResponse("templates/signin.html")


@app.get("/signup")
async def signup_page():
    return FileResponse("templates/signup.html")


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

    return {
        "status": "Success",
        # "message": f"Welcome, {username_placeholder}! You are now registered." NOT NEEDED FOR NOW
    }


@app.post("/signin")
async def handle_signing_in(
    username_email: str = Form(...),
    password: str = Form(...),
):
    # Тепер дані з форми потраплять сюди
    print(f"Login attempt: {username_email}")
    print(f"Password used: {password}")

    return {
        "status": "Success",
        "user": username_email,
        "message": "Logged in successfully",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
