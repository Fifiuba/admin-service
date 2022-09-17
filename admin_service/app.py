from fastapi import FastAPI, Depends
import uvicorn
from admin_service.controllers import admin_controller
from admin_service.security import jwt_handler


app = FastAPI()
app.include_router(admin_controller.admin_route, prefix="/admins", tags=["Admins"])


@app.get("/")
async def read_items():
    return {"token": "Hola"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
