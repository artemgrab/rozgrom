from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import engine
import models
from routers.router_handler import main_router


# Initializing app and toggling on router files
app = FastAPI()
app.include_router(main_router)
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
