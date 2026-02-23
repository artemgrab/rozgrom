from fastapi import FastAPI, Form, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from database import engine, Base
import models
from routers import auth, chat


# Initializing app and toggling on router files
app = FastAPI()
app.include_router(auth.router)
app.include_router(chat.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Create the database tables, look in "models.py"
models.Base.metadata.create_all(bind=engine)


# Exeption handler for unknown pages
@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return FileResponse("templates/404.html")


# Starts up the server on running "main.py" file
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
