from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    return FileResponse('templates/signup.html')

@app.post("/signup")
async def handle_registration(username_placeholder: str = Form(...),
                                email_placeholder: str= Form(...),
                                password_placeholder: str = Form(...),
                                confirm_pasword: str = Form(...)):

    print(f"New User: {username_placeholder}")
    print(f"New User's email: {email_placeholder}")
    print(f"New User's password: {password_placeholder}")
    
    return {
        "status": "Success",
        # "message": f"Welcome, {username_placeholder}! You are now registered." NOT NEEDED FOR NOW
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)